# 6 Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

import math

def is_prime(number):
    if number <= 3:
        return True
    else:
        for num in range(2, int(math.sqrt(number)) + 1):
            if number % num == 0:
                return False
        return True


print(is_prime(7))
print(is_prime(191))
print(is_prime(333))
print(is_prime(1000))
