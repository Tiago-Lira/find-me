import os

from flask import (
    Flask,
    render_template,
    request,
)

from location import LocationTracker


app = Flask(__name__)


@app.route("/")
def index():
    ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    location = LocationTracker().track(ip_address)
    return render_template('index.html', location=location)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
