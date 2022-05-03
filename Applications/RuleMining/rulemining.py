from ink.base.connectors import StardogConnector
from ink.base.structure import InkExtractor
import stardog
from tqdm import tqdm
import six
import sys
sys.modules['sklearn.externals.six'] = six
from skrules import SkopeRules
import pandas as pd


def func1(data):
    features = data[0].tocsc()
    cols = data[2]
    print(data[1])
    drops = set()
    for i in tqdm(range(0, features.shape[1])):
        # if 'real_data' not in cols[i]:
        if features[:, i].sum() == 1 or features[:, i].getnnz() == 1:
            drops.add(i)
    n_cols = [j for j, i in tqdm(enumerate(cols)) if j not in drops]
    return features[:, n_cols], X_train[1], [i for j, i in enumerate(cols) if j not in drops]

if __name__ == '__main__':

    conn_details = {
        'endpoint': 'http://localhost:5820',
        'username': 'admin',
        'password': 'admin'
    }
    connector = StardogConnector(conn_details,'protego_data')
    extractor = InkExtractor(connector, verbose=True)

    with stardog.Connection('protego_data', **conn_details) as conn:
        results = conn.select("""
        select DISTINCT ?a where {
        ?a a <https://saref.etsi.org/saref4ehaw/Activity> .
        } 
        """
        )
    all_activities = set([x['a']['value'] for x in results['results']['bindings']])

    ##### Creating the INK representation

    pos = set(list(all_activities))
    neg = None

    X_train, y_train = extractor.create_dataset(2, pos, neg, jobs=4, skip_list=['http://www.w3.org/1999/02/22-rdf-syntax-ns#type'])
    X_train = extractor.fit_transform(X_train, counts=True, float_rpr=True)
    df = pd.DataFrame.sparse.from_spmatrix(X_train[0], index=X_train[1], columns=X_train[2])

    ##### Start rule mining

    # change activity here you want to predict
    activity = "https://dahcc.idlab.ugent.be/Ontology/ActivityRecognition/WatchingTVActively"


    with stardog.Connection('protego_data', **conn_details) as conn:
        results = conn.select("""
           select DISTINCT ?a where {
           ?a a <""" + activity + """> .
           }
           """)

    pos = set(list(set([x['a']['value'] for x in results['results']['bindings']])))
    neg = set(list(all_activities - pos))


    pos = set(list(set([x['a']['value'] for x in results['results']['bindings']])))
    neg = set(list(all_activities - pos))

    y = [1 if i in pos else 0 for i in df.index]

    clf = SkopeRules(max_depth=3,
                     n_estimators=100,
                     precision_min=0.3,
                     recall_min=0.1,
                     feature_names=df.columns,
                     n_jobs=-1)
    clf.fit(df.values, y, )
    rules = clf.rules_[0:3]
    print(len(clf.rules_))
    for rule in rules:
        print(rule)
    print()
    print(20 * '=')
    print()

