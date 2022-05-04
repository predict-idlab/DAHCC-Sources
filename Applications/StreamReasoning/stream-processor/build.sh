#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# get image name
IMAGE_NAME=local/stream-processor

# build image
sudo docker build -t "$IMAGE_NAME" "$DIR"/image/.

# push to registry
sudo docker push gitlab.ilabt.imec.be:4567/protego/protego-kb-activity-detection/"$IMAGE_NAME"
