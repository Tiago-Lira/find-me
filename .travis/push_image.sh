#!/bin/sh
docker login -u $DOCKER_USERNAME -p $DOCKER_ACCESS_TOKEN

if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

docker build -t $IMAGE_NAME:$TAG .
docker push $IMAGE_NAME:$TAG
