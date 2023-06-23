# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_multiplication(operation, num_rows, num_columns):
    table = []
    for i in range(num_rows):
        incom_list = []
        table.append(incom_list)
        for j in range(num_columns):
            incom_list.append(operation(i + 1, j + 1))
            if j == 0: print(table[i][j], end='')
            else: print(f'\t{table[i][j]}', end='')
        print('\n')

def print_operation_sum(operation, num_rows, num_columns):
    table = []
    for i in range(num_rows):
        incom_list = []
        table.append(incom_list)
        for j in range(num_columns):
            if j == 0:
                incom_list.append(i + 1)
                print(table[i][j], end='')
            elif i == 0:
                incom_list.append(operation(i + 1, j))
                print(f'\t{table[i][j]}', end='')
            else:
                incom_list.append(operation(i + 1, j + 1))
                print(f'\t{table[i][j]}', end='')
        print('\n')

rows = int(input('введите количество строк: '))
columns = int(input('введите количество столбцов: '))
choice = input('введите символ функии построения таблицы (+ или *): ')
if choice == '*':
    print_operation_multiplication(lambda x, y: x * y, rows, columns)
elif choice == '+':
    print_operation_sum(lambda x, y: x + y, rows, columns)
else: print('некорректный ввод или такой функции нет в выборе')