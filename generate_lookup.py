"""
Generate lookup table of MNBT greetings
"""
import pathlib
import json
from typing import Dict
import pendulum
from mnbt import hello_thread
import logging


logger = logging.getLogger(__name__)


_default_output_path = pathlib.Path(__file__).parent / "lookup.json"
_default_start_date = pendulum.date(year=1900, month=1, day=1)
_default_end_date = pendulum.date(year=3000, month=1, day=1)


def create_lookup(path: pathlib.Path = _default_output_path) -> None:
    """Generate and save lookup table to given path (json)"""
    lookup = generate_lookup()
    with path.open('w') as file:
        json.dump(lookup, file, default=str)


def generate_lookup(
        start_date: pendulum.Date = _default_start_date,
        end_date: pendulum.Date = _default_end_date
) -> Dict[str, str]:
    """Generate lookup table of MNBT greetings"""
    day = start_date
    one_day = pendulum.duration(days=1)
    lookup = dict()
    while day <= end_date:
        lookup[day.to_date_string()] = hello_thread(day)
        day = day + one_day
    return lookup


if __name__ == '__main__':
    create_lookup()
