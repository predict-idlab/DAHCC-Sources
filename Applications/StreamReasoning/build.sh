#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# build all images
"$DIR"/stream-processor/build.sh
