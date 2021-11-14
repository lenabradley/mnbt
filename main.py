from flask import Flask
from mnbt import pendulum, hello_thread
import logging


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    return hello_thread(pendulum.today())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
