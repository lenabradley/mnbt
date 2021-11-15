from flask import Flask
from mnbt import pendulum, hello_thread
import logging


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    date = pendulum.today()
    message = hello_thread(date)
    page = f"""
    <center>
    <i>Are you ready for</i>
    <h2>MONDAY NIGHT BEFORE THANKSGIVING?</h2>
    <br><br>
    Today is {date.format("dddd MMMM Do, YYYY")}, {message}
    <br><br>
    <3
    </center>
    """
    return page


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
