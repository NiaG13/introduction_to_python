# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите количество элементов в списке: '))

one_list = []
for i in range(1, n + 1):
    one_list.append(i)

print(*one_list)

x = int(input('Введите число: '))

diff = x
x1 = 0
x2 = 0

for i in one_list:
    if x - i == 0:
        x2 = i
    elif abs(x - i) < diff and abs(x - i) != 0:
        diff = abs(x - i)
        x1 = i

if x2 == x:
    print(f'Имеется равный по величине элемент.')
else:
    print(f'Ближайший по величине элемент равен {x1}.')