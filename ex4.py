# 4 Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит
#  (зима, весна, лето или осень).

def season(months_num):
    if months_num < 3 or months_num == 12:
        return "winter"
    if 2 < months_num < 6:
        return "spring"
    if 5 < months_num < 9:
        return "summer"
    if 8 < months_num < 12:
        return "autumn"


print(season(1))
print(season(3))
print(season(6))
print(season(9))
print(season(12))
print(season(16))
