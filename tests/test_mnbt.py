import pytest
import pendulum
from lib import mnbt


@pytest.mark.parametrize("year, month, day, expected", [
    (2021, 11, 25, "HT!"),
    (2021, 11, 24, "HTW!"),
    (2021, 11, 22, "HMNBT!"),
    (2021, 11, 21, "HSNBMNBT!"),
    (2021, 11, 20, "HSNBMNBT!"),
    (2021, 11, 19, "HFNBMNBT!"),
    (2021, 11, 18, "HTNBMNBT!"),
    (2021, 11, 17, "HWNBMNBT!"),
    (2021, 11, 16, "HTNBMNBT!"),
    (2021, 11, 15, "HMNBMNBT!"),
    (2021, 11, 14, "HSNBMNBMNBT!"),
    (2021, 11,  5, "HFNBMNBMNBMNBT!"),
])
def test_mnbt_day(year: int, month: int, day: int, expected: str):
    """Test mnbt"""
    # Arrange
    date = pendulum.date(year=year, month=month, day=day)

    # Act
    message = mnbt.hello_thread(date)
    print(message)

    # Assert
    assert message == expected


@pytest.mark.parametrize("year, month, day, expected", [
    (2021, 11, 27, False),
    (2021, 11, 26, False),
    (2021, 11, 25, True),
    (2021, 11, 24, True),
    (2021, 11, 23, True),
    (2021, 11, 22, True),
    (2021, 11, 21, False),
    (2021, 11, 20, False),
    (2021, 11, 19, False),
    (2021, 11, 18, False),
    (2021, 11, 17, False),
    (2021, 11, 16, False),
])
def test_is_thanksgiving_week(year: int, month: int, day: int, expected: bool):
    """Test thanksgiving week determination"""
    # Arrange
    date = pendulum.date(year=year, month=month, day=day)

    # Act
    result = mnbt.is_thanksgiving_week(date)

    # Assert
    assert result == expected
