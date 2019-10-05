import os
from logging.config import dictConfig

from flask import (
    Flask,
    render_template,
    request,
)

from find_me.location import LocationTracker


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


@app.route("/")
def index():
    ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    app.logger.info(f'Finding location of {ip_address}')
    location = LocationTracker().track(ip_address)
    app.logger.info(f'Found: {location}')
    return render_template('index.html', location=location)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
