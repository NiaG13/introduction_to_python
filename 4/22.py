# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = [int(i) for i in input().split()]

one_set = []
for i in range(n[0]):
    one_set.append(int(input()))
print(*one_set)
one_set = set(one_set)

two_set = []
for i in range(n[1]):
    two_set.append(int(input()))
print(*two_set)
two_set = set(two_set)

answer = sorted(list(one_set.intersection(two_set)))

print(*answer)
