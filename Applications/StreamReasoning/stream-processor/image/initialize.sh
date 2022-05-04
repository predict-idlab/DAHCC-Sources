#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# wait a while because the RSP server should be properly started first
sleep 5

# do the RSP engine initialization using the config file
python3 "$DIR"/init_rsps.py "$DIR"/rsps.config
