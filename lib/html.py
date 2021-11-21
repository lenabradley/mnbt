import pendulum
import flask
from lib import mnbt, defaults


def generate_index(date: pendulum.Date) -> str:
    """Generate index page html"""
    message = mnbt.hello_thread(date)
    celebration_gif = \
        f'<br><img src="{defaults.celebration_gif_path}" /><br>' \
            if mnbt.is_thanksgiving_week(date) else ""

    return \
        f"""
        <!DOCTYPE html>
        <html>
            <body style="background-color:rosybrown;">
                <center>
                    <br><br>
                    <i>Are you ready for</i>
                    <h2>MONDAY NIGHT BEFORE THANKSGIVING?</h2>
                    <br><br>
                    Today is {date.format("dddd MMMM Do, YYYY")}, {message}
                    {celebration_gif}
                    <p style="font-size:50px">&#129411; &#127810; &#127792; &#127809; &#129383; &#127867; &#10084;</p>
                    <br><br>
                </center>
            </body>
        </html>
        """
