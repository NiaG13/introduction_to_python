# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)

print('Введите количество долек шоколадки по высоте (длине), а затем с новой строки количество долек по ширине.')
n = int(input())

if n < 1: print('Некорректный ввод.')
else:
    m = int(input())
    if m < 1: print('Некорректный ввод.')
    else:
        k = int(input('Введите количество долек шоколадки, которое вы хотите отломить за одно деление: '))
        if k < 1: print('Некорректный ввод.')
        elif k > m * n: print('Это больше чем имеется.')
        elif k == m * n: print('Отламывать не надо, это всё что есть.')
        else:
            if k % m == 0 or k % n == 0: print(f'От шоколадки размером {m}х{n} у вас ПОЛУЧИТЬСЯ отломить за одно деление {k} долек!')
            else: print(f'От шоколадки размером {m}х{n} у вас НЕ получиться отломить за одно деление {k} долек.')