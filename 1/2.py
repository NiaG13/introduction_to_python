# Найдите сумму цифр трехзначного числа.

N = int(input("Введите трёхзначное число: "))

if N < 100 or N > 999:
    print('Введено некорректное число')
else:
    sum = N // 100 + N // 10 % 10 + N % 10
    print(f'Сумма цифр числа {N} равна {sum}.')