#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# generate config
"$DIR"/generate-config-files.sh

# initialize RSP engine using config (in background)
"$DIR"/initialize.sh &

# start RSP engine server
java -jar "$DIR"/rspservice-csparql-1.0-jar-with-dependencies.jar "$DIR"/setup.properties
