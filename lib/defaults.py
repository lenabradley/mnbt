import pathlib
import pendulum

time_zone = pendulum.timezone('EST')
host = "0.0.0.0"
port = 8080
thanksgiving_week_message = "HTW!"
thanksgiving_day_message = "HT!"
thanksgiving_week_messages = {thanksgiving_week_message, thanksgiving_day_message, "HMNBT!"}