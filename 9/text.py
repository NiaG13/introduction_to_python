main_menu = ['Главное меню:',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

select_menu = 'Выберите пункт меню: '

input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu) - 1}'

new_contact = {'name': 'Введите имя контакта: ',
               'phone': 'Введите телефон: ',
               'comment': 'Введите комментарий: '}

empty_book = 'Телефонная книга пуста или не открыта'

load_successful = 'Телефонная книга успешно загружена!'

save_successful = 'Телефонная книга успешно сохранена!'

error_load = 'Ошибка загрузки телефонной книги!'

error_save = 'Ошибка сохранения телефонной книги!'

search_word = 'Введите строку для поиска: '

choice_changeble_contact = 'Введите индекс контакта для изменения: '

contact_changes = {'name': 'Введите новое имя контакта: ',
                   'phone': 'Введите новый телефон: ',
                   'comment': 'Введите новый комментарий: '}

choice_deleted_contact = 'Введите индекс контакта, который хотите удалить: '

end_message = 'До новых встреч!'


def add_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен в книгу!'

def empty_search(word: str) -> str:
    return f'Контакты содержащие {word} не найдены.'

def error_choice(index: str) -> str:
    return f'Контакта с индексом {index} нет в результатах поиска.'

def successful_change(name: str) -> str:
    return f'Контакт "{name}" успешно изменён!'

def successful_delet(name:str) -> str:
    return f'Контакт "{name}" удалён.'