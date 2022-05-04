import time
import urllib.parse
import requests
from sys import argv
from websocket import create_connection
from time import sleep
from datetime import datetime
import pandas as pd
from mapper import map_observation

DEBUG = False

QUERY_REGISTRATION_URL = "http://%s:%s/queries/%s"
# Query template
QUERY_TEMPLATE = "REGISTER STREAM %s AS %s"


def register_query(host, port, query, query_name):
    """
    Register all given queries at the RSP service.
    :param host: IP of RSP service
    :param port: port of RSP service
    :param queries: queries to be registered
    """
    try:
        # read query file in spec
        print("Register query '%s'" % query_name)
        # perform PUT request to query registration URL to register query (with query content in body)
        put_request(QUERY_REGISTRATION_URL % (host, port, query_name), QUERY_TEMPLATE % (query_name, query))
        time.sleep(1)
    except:
        print("failed to register query %s" % query)


def put_request(url, data):
    """
    Performs HTTP PUT request.

    :param url: URL to which the request should be performed
    :param data: request body content for PUT request
    """

    print("  [%f] POST %s %s" % (time.time(), url, data))
    r = requests.put(url, data)


if __name__ == "__main__":
    # read RSP service config details
    host = "localhost"
    port = 8175


    # register query
    with open('query.ttl','r') as f:
        query = f.read()
    register_query(host, port, query, "showerrule")


    ws_port = 8174
    stream = "http://protego.ilabt.imec.be/idlab.homelab"

    url = "ws://%s:%s/streams/%s" % ('localhost', ws_port, urllib.parse.quote("http://protego.ilabt.imec.be/idlab.homelab", safe=''))
    # create WebSocket connection to main stream URL
    ws = create_connection(url)
    print("Opened WebSocket connection to RSP engine stream WebSocket exposed at %s" % url)

    # read example raw data
    d1 = pd.read_feather("locations.feather")
    d2 = pd.read_feather("humidity.feather")

    df = pd.concat([d1,d2])
    df = df.sort_values("Timestamp")

    time_now = datetime.now()
    last = None
    print("Start ingesting observations")
    for index, row in df.iterrows():
        time_utc = datetime.combine(time_now.date(),row.Timestamp)
        # transform raw data into semantic observations
        event = map_observation(row.Metric, "patient157."+row.Sensor, row.Value, time_utc.timestamp() * 1000)
        if last is not None:
            sleep((time_utc - last).seconds/100)
        last = time_utc
        ws.send(event)
        # sleep to have only periodic events
