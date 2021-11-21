import pendulum


def generate_index(date: pendulum.Date, message: str) -> str:
    """Generate index page html"""
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
                    <br><br>
                    <p style="font-size:50px">&#129411; &#127810; &#127792; &#127809; &#129383; &#127867; &#10084;</p>
                </center>
            </body>
        </html>
        """
