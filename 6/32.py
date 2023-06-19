# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('введите количество элементов в списке: '))

list_one = []
for i in range(n):
    list_one.append(random.randint(0,100))

print(*list_one)

min_list = int(input('введите минимум диапазона поиска: '))
max_list = int(input('введите максимум диапазона поиска: '))

for i in list_one:
    if i >= min_list and i <= max_list:
        print(list_one.index(i), end = ' ')