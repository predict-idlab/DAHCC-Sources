### Guide to run the semantic stream reasoning applications

A stream reasoning application was built to reason upon a predefined rule within a stream of observations.
Here, we defined a shower rule which triggers when a participant is within the bathroom and the humidity level of a specific sensor passes a certain threshold.

To make sure you can run this application, the following software must be installed:
- [Docker](https://docs.docker.com) used to minimize the software dependencies
- [Docker compose](https://docs.docker.com/compose/install/)


To run this applications:
1) open a terminal window and build the stream-processor image (simply run ./build.sh)
2) Start the stream-processor container: `docker-compose -f docker-compose.yml --env-file activity-detection.env up`
   This will create the rspservice-csparql processing unit to handle the streaming events
3) Open a new terminal window and run the monitor tool. This monitor tool returns the constructed events which are triggerd upon the defined query (in query.tt)
   Navigate within the terminal to the monitor folder and execute: `./run-http-monitor.sh 8189 /reasoningservice/stream`
4) Open a third terminal window and run the main.py python script. This script will register the defined query (query.ttl) onto our stream-processing unit
   and will load and transform raw data (.feather files) into semantic observations and send them to the c-sparql engine.

When everything is up and running, you should see observations being evaluated inside the stream-processing terminal and eventually (after some time) see the
constructed events in the monitor terminal.
