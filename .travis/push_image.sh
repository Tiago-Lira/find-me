#!/bin/sh
echo "$DOCKER_ACCESS_TOKEN" | docker login -u $DOCKER_USERNAME --password-stdin

if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

docker build -t $IMAGE_NAME:$TAG .
docker push $IMAGE_NAME:$TAG
