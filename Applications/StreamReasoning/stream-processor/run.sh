#!/bin/bash

WORKING_DIR=$(pwd)
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# get image name
IMAGE_NAME=stream-processor

# stop container
docker stop "$IMAGE_NAME"
docker rm "$IMAGE_NAME"

# run container
docker run --network host --name "$IMAGE_NAME" -v "$WORKING_DIR"/logs:/root/rsps/logs gitlab.ilabt.imec.be:4567/protego/protego-kb-activity-detection/local/"$IMAGE_NAME":latest
