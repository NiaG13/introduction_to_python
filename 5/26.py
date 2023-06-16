# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponent(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    return n * exponent(n, m - 1)

a = int(input('Введите чило а: '))
b = int(input('Введите число b: '))

print(f'{a} ^ {b} = {exponent(a, b)}')