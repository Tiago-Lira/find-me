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
    location = LocationTracker().track(request)
    return render_template('index.html', location=location)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
