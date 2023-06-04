# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число: '))
if N < 2: print('Некорректный ввод.')
else:
    result1 = 1
    print(result1, end = ' ')
    result = 0
    while result < N:
        result1 = result1 * 2
        print(result1, end = ' ')
        result = result1 * 2
    