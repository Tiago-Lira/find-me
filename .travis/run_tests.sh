#!/bin/sh

if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

docker build -t $IMAGE_NAME:$TAG .
docker run -t $IMAGE_NAME:$TAG pytest -v
