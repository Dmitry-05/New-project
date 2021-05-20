# 1 Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними. Если третий
# аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить
# (первое на второе). В остальных случаях вернуть строку "Неизвестная операция"

def arithmetic(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        return num1 / num2
    else:
        return "Unknown operation"
