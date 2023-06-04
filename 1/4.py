# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = int(input('Введите количество сделаных журавликов: '))

if S <= 0: print('Количество не может быть отрицательным.')
elif S < 6: print('Слишком маленькое количество, по условию производительности детей.')
else:
    petya = S // 6
    katya = petya * 4
    ostatok = S % 6
    if S % 6 == 0: print(f'Дети сделали следующее количество журавликов: Петя и Серёжа по {petya}, а Катя {katya}.')
    elif S % 6 != 0: print(f'Дети сделали следующее количество журавликов: Петя и Серёжа по {petya}, а Катя {katya}. {ostatok} шт. кто-то подкинул.')