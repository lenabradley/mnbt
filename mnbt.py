"""
Script to celebrate the Monday night before Thanksgiving
"""
import logging
import pendulum


logger = logging.getLogger(__name__)


def get_next_american_thanksgiving(date: pendulum.Date) -> pendulum.Date:
    """ Get the date of the next thanksgiving in the future, starting from the given date

    If the given date is Thanksgiving, return that date
    """
    start_date = date
    if is_american_thanksgiving(date):
        return date

    one_day = pendulum.Duration(days=1)
    for _ in range(366 + 30 + 1):
        date += one_day

        if is_american_thanksgiving(date):
            return date

    raise ValueError(f"Thanksgiving not found. Input date: {start_date}. End date: {date}")


def is_american_thanksgiving(date: pendulum.Date) -> bool:
    """ Return true if given date is Thanksgiving (4th Thursday of November)"""
    # Thanksgiving is in November
    if date.month != 11:
        return False

    # Thanksgiving is a Thursday
    if date.day_of_week != pendulum.THURSDAY:
        return False

    # Thanksgiving is the 4th Thursday
    num_thursdays = 0
    for day in range(1, date.day + 1):
        tmp_date = pendulum.Date(
            year=date.year,
            month=date.month,
            day=day
        )
        if tmp_date.day_of_week == pendulum.THURSDAY:
            num_thursdays += 1

    if num_thursdays == 4:
        return True

    else:
        return False


def num_mondays_before_thanksgiving(date: pendulum.Date) -> int:
    """ Return the number of weeks before the Monday night before Thanksgiving

    Start looking forward from the given date
    If the given date is Thanksgiving return that date
    """
    next_thanksgiving = get_next_american_thanksgiving(date)
    days_until_thanksgiving = (next_thanksgiving - date).in_days()
    mondays_until_thanksgiving = max(0, (days_until_thanksgiving + 4) // 7)

    return mondays_until_thanksgiving


def hello_thread(today: pendulum.Date) -> str:
    """ Say happy monday before Thanksgiving to the thread! """

    mondays_until_thanksgiving = num_mondays_before_thanksgiving(today)

    # If just a few days to go...
    if mondays_until_thanksgiving < 1:
        if is_american_thanksgiving(today):
            # Happy Thanksgiving
            return "HT!"
        else:
            # Happy Thanksgiving week
            return "HTW!"

    # Its not quite thanksgiving yet... How many mondays to go?
    message_end = ("MNB" * mondays_until_thanksgiving) + "T!"
    if today.day_of_week is pendulum.TUESDAY:
        return "HTNB" + message_end
    if today.day_of_week is pendulum.WEDNESDAY:
        return "HWNB" + message_end
    if today.day_of_week is pendulum.THURSDAY:
        return "HTNB" + message_end
    if today.day_of_week is pendulum.FRIDAY:
        return "HFNB" + message_end
    if today.day_of_week is pendulum.SATURDAY:
        return "HSNB" + message_end
    if today.day_of_week is pendulum.SUNDAY:
        return "HSNB" + message_end
    # Must be Monday
    return "H" + message_end


if __name__ == '__main__':
    date = pendulum.date(2020, 11, 15)
    message = hello_thread(date)
    print(f"Today is {date.to_formatted_date_string()}. {message}")
