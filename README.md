# Monday Night Before Thanksgiving (MNBT)

Say hello to the thread according to the MNBT

## Setup environment
```bash
poetry install
```

## Example usage
```python
import pendulum
from mnbt import hello_thread

date = pendulum.date(year=2011, month=11, day=16)
message = hello_thread(date)
print(message)
```
Prints  "HMNBMNBT!"
