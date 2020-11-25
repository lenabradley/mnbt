"""
Script to celebrate the Monday night before Thanksgiving
"""

import pendulum


def get_next_american_thanksgiving(date: pendulum.Date) -> pendulum.Date:
    """ Get the date of the next thanksgiving in the future, starting from the given date

    If the given date is Thanksgiving, return that date
    """
    if is_american_thanksgiving(date):
        return date

    one_day = pendulum.Duration(days=1)
    for _ in range(365):
        date += one_day

        if is_american_thanksgiving(date):
            return date

    raise ValueError("Thanksgiving not found")


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


def is_monday_before_thanksgiving(date: pendulum.Date) -> bool:
    """ Return true if given date is the Monday before Thanksgiving """
    if is_american_thanksgiving(date + pendulum.Duration(days=3)):
        return True
    return False


def num_mondays_before_thanksgiving(date: pendulum.Date) -> int:
    """ Return the number of weeks before the Monday night before Thanksgiving

    Start looking forward from the given date
    If the given date is Thanksgiving return that date
    """
    next_thanksgiving = is_american_thanksgiving(date)
    days_until_thanksgiving = (next_thanksgiving - date).in_days()
    mondays_until_thanksgiving = max(0, (days_until_thanksgiving + 4) // 7)

    return mondays_until_thanksgiving


def hello_thread():
    """ Say hello to the thread! """

    today = pendulum.today() - pendulum.duration(days=1)
    mondays_until_thanksgiving = num_mondays_before_thanksgiving(today)

    if today.day_of_week != pendulum.MONDAY:
        if is_american_thanksgiving(today):
            message = "Happy Thanksgiving!"
        else:
            if mondays_until_thanksgiving < 1:
                message = "Happy Thanksgiving Week!"
            else:
                message = "beerbarnchickengood"

    else:
        message = f"H" + ("MNB" * mondays_until_thanksgiving) + "T!"

    print(message)


if __name__ == '__main__':
    hello_thread()
