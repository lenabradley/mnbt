from flask import Flask
from mnbt import pendulum, hello_thread
import logging


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    date = pendulum.today()
    message = hello_thread(date)
    f"""
    
    ~~~ MONDAY NIGHT BEFORE THANKSGIVING ~~~
    
    Today is {date.to_day_datetime_string()}, {message}
    
    <3
    
    """

    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
