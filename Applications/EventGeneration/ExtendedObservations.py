import stardog
from tqdm import tqdm
import pandas as pd
tqdm.pandas()
from mapper import map_observation, generate_actid,map_activities, map_value, map_phone_action
import datetime
from glob import glob
from multiprocessing import Pool


conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}

def generate_observation_triple(row, user):
    time = datetime.datetime.combine(datetime.date(2022, 1, 3),row.Timestamp).strftime('%Y-%m-%dT%H:%M:%S.%f')
    obs, time_str, triple = map_observation(row.Metric,row.Sensor,user,time,row.Value)
    return triple, obs, time_str

def add_data_triplestore(conn, triple):
    conn.begin()
    conn.add(stardog.content.Raw(triple))
    conn.commit()

def delete_data_triplestore(conn, triple):
    conn.begin()
    conn.remove(stardog.content.Raw(triple))
    conn.commit()

def reason(conn, obs):
    res = conn.select('select ?o where { '+obs+' <https://dahcc.idlab.ugent.be/Ontology/SensorsAndActuators/actsLike> ?o }', reasoning=True)
    if len(res['results']['bindings'])>0:
        command = res['results']['bindings'][0]['o']['value']
    else:
        command = None
    return command

def query_meta(conn, obs):
    query = """
    select ?u ?a where {
        """+obs+""" <https://saref.etsi.org/core/measurementMadeBy> ?s .
        ?s a ?a .
        ?s <https://dahcc.idlab.ugent.be/Ontology/SensorsAndActuators/analyseStateOf> ?u .
    }"""
    return conn.select(query)['results']['bindings']

def get_sensor_room(conn, sensor):
    query = """
    select ?r where {
        <https://dahcc.idlab.ugent.be/Homelab/SensorsAndActuators/"""+sensor+"""> <https://saref.etsi.org/saref4bldg/isContainedIn> ?r .
    }"""
    return conn.select(query)['results']['bindings'][0]['r']['value'].split('/')[-1]

def main(file='/_participant6/data.feather'):
    #read feather file into dataframe
    df = pd.read_feather(file)
    #add a date, so we can later on filter on dates
    df['Date'] = df.Timestamp.apply(lambda x: datetime.datetime.combine(datetime.date(2022, 1, 3),x))
    df = df.groupby(['Sensor', pd.Grouper(key='Date', freq='1T')]).tail(1)
    #check for specific metrics
    if any(ext in file for ext in set(['environment.open', 'energy.power', 'environment.waterRunning::bool','people.presence.detected','environment.motion'])):
        df.Value = df.Value.astype(float)
        df = df[df.Value>0]
    user = file.split('/')[-3]

    # create stardog database (based on the participant's name)
    with stardog.Admin(**conn_details) as admin:
        try:
            db = admin.new_database(user.replace('_',''), {'strict.parsing': False})
        except:
            db = admin.database(user.replace('_',''))
            db.drop()
            db = admin.new_database(user.replace('_',''), {'strict.parsing': False})


    with stardog.Connection(user.replace('_',''), **conn_details) as conn:
        # add rule.ttl to stardog database
        conn.begin()
        conn.add(stardog.content.File('rule.ttl'))
        conn.commit()

        # add full protego dahcc ontology to dataset
        conn.begin()
        conn.add(stardog.content.File('protego_dahcc.owl'))
        conn.commit()

        with stardog.Admin(**conn_details) as admin:
            db = admin.database(user.replace('_',''))
            db.optimize()

        #iterate over the rows of the dataframe and create the desired triples based on the dahcc ontology
        for i, row in tqdm(df.iterrows(), total=len(df)):
            triple, obs, time = generate_observation_triple(row, user)
            # add those triples to the stardog database
            add_data_triplestore(conn, triple)
            # execute the reasoning query
            reason_res = reason(conn, obs)
            if reason_res is not None:
                id = generate_actid(user)
                s = ''
                res = query_meta(conn, obs)
                if len(res)>0:
                    for a in res:
                        if 'NamedIndividual' in a['a']['value']:
                            continue
                        if 'StartCommand' in reason_res:
                            met = 'using'
                        elif 'NotifyCommand' in reason_res:
                            met = 'personIn'
                        elif 'OnCommand' in reason_res:
                            met = a['a']['value'].split('/')[-1]+'LightSwitchedOnIn'
                        elif 'OffCommand' in reason_res:
                            met = a['a']['value'].split('/')[-1]+'LightSwitchedOffIn'
                        elif 'CloseCommand' in reason_res:
                            met = 'closing'
                        else:
                            met = 'opening'
                        s += "<http://protego.idlab.imec.be/%s/event%s> <https://dahcc.idlab.ugent.be/Ontology/SensorsAndActuators/%s> <%s> .\n"%(user, id, met, a['u']['value'])

                    t = "<http://protego.idlab.imec.be/%s/event%s> <https://dahcc.idlab.ugent.be/protego/atTime> %s .\n"%(user, id, time)
                    u = '<http://protego.idlab.imec.be/%s/event%s> <https://dahcc.idlab.ugent.be/protego/by> <http://protego.idlab.imec.be/usr%s> .\n'%(user, id, user)

                    # create new events based upon the reasonong results
                    with open("events"+user+".nt", "a") as f:
                        f.write(s)
                        f.write(t)
                        f.write(u)

                delete_data_triplestore(conn, triple)

def netatmo(file="/_participant6/sensors/"):
    netatmos = ["70:ee:50:67:3e:78", "70:ee:50:67:3e:78", "70:ee:50:67:30:b2", "70:ee:50:67:30:60", "70:ee:50:67:2e:2c", "70:ee:50:63:da:32", "70:ee:50:63:d9:c0"]
    user = file.split('/')[-3]

    with stardog.Admin(**conn_details) as admin:
        try:
            db = admin.new_database(user.replace('_',''), {'strict.parsing': True})
        except:
            db = admin.database(user.replace('_',''))
            db.drop()
            db = admin.new_database(user.replace('_',''), {'strict.parsing': True})

    with stardog.Connection(user.replace('_',''), **conn_details) as conn:
        ## init
        conn.begin()
        conn.add(stardog.content.File('rule.ttl'))
        conn.commit()

        conn.begin()
        conn.add(stardog.content.File('/Users/bramsteenwinckel/Documents/repos/protego-ontology/full.owl'))
        conn.commit()

    for n in netatmos:
        df = pd.read_feather(file+n+".feather")
        ###
        with stardog.Connection(user.replace('_',''), **conn_details) as conn:
            room = get_sensor_room(conn, n)
        ###
        id = generate_actid(user)
        for i, row in df.iterrows():
            id = generate_actid(user)
            time = datetime.datetime.combine(datetime.date(2022, 1, 3),row.Timestamp).strftime('%Y-%m-%dT%H:%M:%S.%f')
            s = "<http://protego.idlab.imec.be/%s/sensor%s> <https://dahcc.idlab.ugent.be/data/%s/%s> %s .\n"%(user, id, room, row['Metric'], map_value(row['Value'], row['Metric'])[0])
            t = '<http://protego.idlab.imec.be/%s/sensor%s> <https://dahcc.idlab.ugent.be/Ontology/atTime> "%s"^^<http://www.w3.org/2001/XMLSchema#dateTime> .\n'%(user, id, time)
            u = '<http://protego.idlab.imec.be/%s/sensor%s> <https://dahcc.idlab.ugent.be/Ontology/by> <http://protego.idlab.imec.be/usr%s> .\n'%(user, id, user)
            with open("sensordata"+user+".nt", "a") as f:
                f.write(s)
                f.write(t)
                f.write(u)

def fix_time(x):
    try:
         return datetime.datetime.strptime(x, '%H:%M:%S.%f').time()
    except:
        return datetime.datetime.strptime(x, '%H:%M:%S').time()

def main_activity(file='/_participant6/labels.csv'):
    user = file.split('/')[-2]
    df = pd.read_csv(file, index_col=0)

    df['start_time'] = df['start_time'].apply(fix_time)
    df['end_time'] = df['end_time'].apply(fix_time)
    with open("activities.nt", "a") as f:
        def write_activity(row):
            f.write(map_activities(user,row.ontology_label,datetime.datetime.combine(datetime.date(2022, 1, 3),row.start_time).strftime('%Y-%m-%dT%H:%M:%S.%f'), datetime.datetime.combine(datetime.date(2022, 1, 3),row.end_time).strftime('%Y-%m-%dT%H:%M:%S.%f')))

        df.progress_apply(lambda row: write_activity(row), axis=1)

def post_process():
    with stardog.Admin(**conn_details) as admin:
        try:
            db = admin.new_database('protego_data', {'strict.parsing': False})
        except:
            db = admin.database('protego_data')
            db.drop()
            db = admin.new_database('protego_data', {'strict.parsing': False})


    with stardog.Connection('protego_data', **conn_details) as conn:
        conn.begin()
        conn.add(stardog.content.File('activities.nt'))
        conn.commit()
        for file in tqdm(glob('/Users/bramsteenwinckel/Datasets/Protego_anom/*/')):
            conn.begin()
            user = file.split('/')[-2]
            conn.add(stardog.content.File('events'+user+'.nt'))
            conn.commit()

            conn.begin()
            user = file.split('/')[-2]
            conn.add(stardog.content.File('sensordata'+user+'.nt'))
            conn.commit()

        for file in tqdm(glob('/Users/bramsteenwinckel/Datasets/Protego_anom/*/')):
            usr = file.split('/')[-2]
            query="""
            select ?s ?a where {
                ?a <https://dahcc.idlab.ugent.be/Ontology/by> <http://protego.idlab.imec.be/usr"""+usr+"""> .
                <http://protego.idlab.imec.be/usr"""+usr+"""> <https://saref.etsi.org/saref4ehaw/hasActivity> ?s .
                ?s <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/activityStart> ?b.
                ?s <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/activityEnd> ?e.
                ?a <https://dahcc.idlab.ugent.be/Ontology/atTime> ?t .
                FILTER(?t<?e && ?t>?b) .
            }
            """
            with open('links.nt', 'a') as f:
                for row in conn.select(query)['results']['bindings']:
                    f.write('<'+row['s']['value']+'> <https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/hasEvent> <'+row['a']['value']+'> .\n')

        conn.begin()
        conn.add(stardog.content.File('links.nt'))
        conn.commit()


def _proc(user):
    for metric in set(['environment.open', 'energy.power', 'environment.waterRunning::bool','people.presence.detected','environment.motion','environment.lightswitch','environment.blind']):
        try:
            main(user+'metrics/'+metric+'.feather')
        except:
            None


if __name__ == '__main__':
    # get activity labels
    for file in glob('protego/*/labels.csv'):
         main_activity(file)
    # transform data and create new events
    data = list(glob('protego/*/'))
    with Pool(6) as pool:
         res = list(tqdm(pool.imap_unordered(_proc, data, chunksize=1), total=len(data)))
         pool.close()
         pool.join()
         
    # link activities and events together
    post_process()
