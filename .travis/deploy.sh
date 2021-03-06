#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
echo "$HEROKU_API_KEY" | docker login -u _ --password-stdin registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME
