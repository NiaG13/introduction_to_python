import json


phone_book = {}
path = 'phones.json'


def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False  


def save_file():
    try:
        with open(path, 'w', encoding='UTf-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False


def add_contact(new: dict[str,str]):
    contact = {check_id(): new}
    phone_book.update(contact)


def check_id() -> int:
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1


def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result


def check_contact(index: int, incoming_book: dict[int:dict[str,str]]):
    if index in incoming_book:
        return True
    return False


def changed_contact(index: int, changes_cnt: dict[int:dict[str,str]]) -> dict[str,str]:
    global phone_book
    old_cnt = phone_book[index]
    for key in changes_cnt:
        if changes_cnt[key] == '':
            changes_cnt[key] = old_cnt[key]
    phone_book[index] = changes_cnt
    return phone_book[index]


def delet_contact(index: int) -> dict[str,str]:
    global phone_book
    del_cnt = phone_book[index]
    phone_book.pop(index)
    return del_cnt