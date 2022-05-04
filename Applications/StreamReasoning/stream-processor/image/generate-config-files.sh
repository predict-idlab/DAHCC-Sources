#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# create rsps.config file
# -> used for stream & observer registration
envsubst < ${DIR}/rsps.config.template > ${DIR}/rsps.config

# create setup.properties file
# -> used for starting up the RSP engine system itself
envsubst < ${DIR}/setup.properties.template > ${DIR}/setup.properties
