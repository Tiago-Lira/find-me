import os
from logging.config import dictConfig

from flask import Flask, render_template

from find_me.geolocation import GLocationFinder
from find_me.ipstack import IPStackAPI
from find_me.utils import get_client_ip_address


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

glocation = GLocationFinder(IPStackAPI())


@app.route("/")
def index():
    ip_address = get_client_ip_address()
    app.logger.info(f'Finding location for ip {ip_address}')
    result = glocation.find(ip_address)
    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
