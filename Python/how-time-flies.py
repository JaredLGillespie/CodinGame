# https://www.codingame.com/training/easy/how-time-flies


from datetime import datetime
from dateutil.relativedelta import relativedelta


def solution():
    begin = datetime.strptime(input(), '%d.%m.%Y')
    end = datetime.strptime(input(), '%d.%m.%Y')

    delta = relativedelta(end, begin)
    years = delta.years
    months = delta.months
    days = (end - begin).days

    f = lambda x: 's' if x != 1 else ''
    if years > 0: print('{} year{}, '.format(years, f(years)), end='')
    if months > 0: print('{} month{}, '.format(months, f(months)), end='')
    print('total {} day{}'.format(days, f(days)), end='')


solution()
