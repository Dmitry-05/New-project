# 7 Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.

def date(day, month, year):
    if month == 2:
        if year % 4 == 0:
            return months_changes(day, 29)
        else:
            return months_changes(day, 28)
    elif month % 2 == 1:
        return months_changes(day, 31)
    elif month % 2 == 0:
        return months_changes(day, 30)


def months_changes(day, max_days):
    if day < max_days + 1:
        return True
    else:
        return False


print(date(31, 1, 2000))
print(date(32, 1, 2000))
print(date(29, 2, 2004))
print(date(29, 2, 2006))
print(date(30, 4, 2000))
print(date(31, 4, 2000))
