import pathlib
import pendulum

time_zone = pendulum.timezone('EST')
host = "0.0.0.0"
port = 8080
celebration_gif_path = pathlib.Path(__file__).parent.parent / "data" / "celebration.gif"
thanksgiving_week_message = "HTW!"
thanksgiving_day_message = "HT!"
thanksgiving_week_messages = {thanksgiving_week_message, thanksgiving_day_message, "HMNBT!"}