#!/bin/sh

if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi

docker build -t $TRAVIS_REPO_SLUG:$TAG .
docker run -t $TRAVIS_REPO_SLUG:$TAG pytest -v
