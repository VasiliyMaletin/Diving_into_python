from datetime import datetime as dt
from calendar import isleap
from sys import argv

__all__ = ['check_date', 'check_year']


def check_date(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
        dt(year=year, month=month, day=day)
    except:
        return False
    return True


def check_year(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    return isleap(year)


def check_date_terminal():
    date = argv[1]
    result = check_date(date)
    return result

if __name__ == '__main__':
    print(check_date('24.11.2020'))
    print(check_year('14.11.2000'))
