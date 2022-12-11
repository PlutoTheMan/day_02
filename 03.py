from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pl_PL.UTF-8')


def format_date(day, month, year):
    ret = None
    try:
        time = datetime(year, month, day)
        ret = time.strftime("%d %B %Y")
    except ValueError:
        pass

    return ret


print(format_date(22, 2, 1993))
