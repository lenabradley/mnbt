from flask import Flask
import pendulum
from lib import html, defaults
import logging


logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def index():
    date = pendulum.today(tz=defaults.time_zone)
    page = html.generate_index(date=date)
    return page


if __name__ == "__main__":
    app.run(host=defaults.host, port=defaults.port, debug=True)
