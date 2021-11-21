from flask import Flask
import pendulum
from lib import mnbt, html, defaults
import logging


logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def index():
    date = pendulum.today(tz=defaults.time_zone)
    message = mnbt.hello_thread(date)
    page = html.generate_index(date=date, message=message)
    return page


if __name__ == "__main__":
    app.run(host=defaults.host, port=defaults.port, debug=True)
