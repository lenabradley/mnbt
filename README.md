# Monday Night Before Thanksgiving (MNBT)

Say hello to the thread and celebrate the Monday Night Before (American) Thanksgiving 

## Setup python environment
Using python 3.6+

```bash
./bin/setup_env.sh
```

To activate venv:
```shell
source venv/bin/activate
```

## Example python usage
```python
import pendulum
from mnbt import hello_thread

date = pendulum.date(year=2011, month=11, day=16)
message = hello_thread(date)
print(f"Today is {date.to_formatted_date_string()}. {message}")

# Prints "Today is Nov 15, 2020. HSNBMNBMNBT!"
```

## Run app


To run the flask app via gunicorn:
```shell
./bin/run_app.sh
```
