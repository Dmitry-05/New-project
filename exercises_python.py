# 1 Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними. Если третий
# аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить
# (первое на второе). В остальных случаях вернуть строку "Неизвестная операция"

# def arithmetic(num1, num2, oper):
#     if oper == "+":
#         return num1 + num2
#     elif oper == "-":
#         return num1 - num2
#     elif oper == "*":
#         return num1 * num2
#     elif oper == "/":
#         return num1 / num2
#     else:
#         return "Unknown operation"

# 2 Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(is_year_leap(2000))
print(is_year_leap(2001))
