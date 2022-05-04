import time
import urllib.parse
import requests
from sys import argv
from backports import configparser

DEBUG = False

# URL templates
STREAM_REGISTRATION_URL = "http://%s:%s/streams/%s"
STREAM_WS_REGISTRATION_URL = "http://%s:%s/streams/%s/ws"
QUERY_REGISTRATION_URL = "http://%s:%s/queries/%s"
OBSERVER_REGISTRATION_URL = "http://%s:%s/observers"
QUERY_OBSERVER_REGISTRATION_URL = "http://%s:%s/queries/%s/observers"

# Query template
QUERY_TEMPLATE = "REGISTER STREAM %s AS %s"


def read_config_file(filename):
    """
    Reads in the given config file.

    :param filename: config file
    :return: config details as ordered dictionaries
    """

    # create config parser with given delimiter
    config = configparser.ConfigParser(delimiters='?')
    # parse config file
    config.read(filename)
    # return config details as ordered dictionaries
    return config._sections


def register_streams(host, port, streams):
    """
    Register all given streams at the RSP service.

    :param host: IP of RSP service
    :param port: port of RSP service
    :param streams: streams to be registered
    """
    for stream in streams:
        urls = streams[stream].split(',')

        stream_url = urls[0]
        if DEBUG:
            print("Register stream '%s' (%s)" % (stream, stream_url))
        # perform PUT request to stream registration URL to register stream
        put_request(STREAM_REGISTRATION_URL % (host, port, urllib.parse.quote(stream_url, safe='')), '')
        time.sleep(1)

        if len(urls) > 1:
            ws_url = urls[1]
            if DEBUG:
                print("Register WebSocket server for stream '%s'" % stream)
            put_request(STREAM_WS_REGISTRATION_URL % (host, port, urllib.parse.quote(stream_url, safe='')), ws_url)


def register_queries(host, port, queries):
    """
    Register all given queries at the RSP service.

    :param host: IP of RSP service
    :param port: port of RSP service
    :param queries: queries to be registered
    """
    for query in queries:
        path = queries[query]
        try:
            # read query file in spec
            f = open(path)
            spec = f.read()
            if DEBUG:
                print("Register query '%s'" % query)
            # perform PUT request to query registration URL to register query (with query content in body)
            put_request(QUERY_REGISTRATION_URL % (host, port, query), QUERY_TEMPLATE % (query, spec))
            time.sleep(1)
        except:
            if DEBUG:
                print("failed to register query %s" % query)


def register_observers(host, port, observers):
    """
    Register all given observers at the RSP service.
    An observer consists of:
     - the stream which is observing query results (i.e. to which query results should be sent)
     - the queries of which the results should be observed
       (if this is 'all', then the observer is registered as a general observer of the RSP engine)

    :param host: IP of RSP service
    :param port: port of RSP service
    :param observers: observers to be registered
    """
    for observer in observers:
        # obtain list of all queries of which the results should be observed
        if observers[observer] == 'all':
            if DEBUG:
                print("Register general observer '%s' for RSP engine" % observer)
            # register stream URL as observer to query results by performing POST request
            put_request(OBSERVER_REGISTRATION_URL % (host, port), observer)
            time.sleep(1)

        else:
            queries = [q.strip() for q in observers[observer].split(',')]
            for query in queries:
                if DEBUG:
                    print("Register observer '%s' for query '%s'" % (observer, query))
                # register stream URL as observer to query results by performing POST request
                put_request(QUERY_OBSERVER_REGISTRATION_URL % (host, port, query), observer)
                time.sleep(1)


def put_request(url, data):
    """
    Performs HTTP PUT request.

    :param url: URL to which the request should be performed
    :param data: request body content for PUT request
    """
    if DEBUG:
        print("  [%f] POST %s %s" % (time.time(), url, data))
    r = requests.put(url, data)
    if DEBUG:
        print("  [Response: %s] %s %r" % (time.time(), r.status_code, r.text))


if __name__ == "__main__":
    # read config file
    _config = read_config_file(str(argv[1]))

    # read RSP service config details
    rsp_service = _config["rspservice"]
    _host = rsp_service["host"]
    _port = rsp_service["port"]

    # register streams
    register_streams(_host, _port, _config["streams"])

    # register queries
    register_queries(_host, _port, _config["queries"])

    # register observers
    register_observers(_host, _port, _config["observers"])
