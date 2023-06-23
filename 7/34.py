# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# **Вывод:** Парам пам-пам

def count_vowel(phrase):
    vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for i in phrase:
        if i in vowel:
            count += 1
    return count
    
def count_rhyme(list_1):
    count_r = list(map(lambda x: count_vowel(x), list_1))
    rhyme = 0
    for i in range(len(count_r)):
        if count_r[i - 1] != count_r[i]:
            rhyme +=1
    if rhyme == 0: print('Парам пам-пам')
    else: print('Пам парам')


poem = input('Введите стихотворение: ').lower().split()
count_rhyme(poem)
