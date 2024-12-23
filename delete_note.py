from wsgiref.util import request_uri

from display_notes_function import display_notes
from Data import generate_notes, print_

@print_
def delete_notes_by_criteria(list_notes, val):
    if not list_notes:
        print("Список заметок пуст!")
        return list_notes

    res = list(filter(lambda x: x.get("username").strip().lower() != val.lower() and
                      x.get("title").strip().lower() != val.lower(),
                      list_notes))
    if len(res) != len(list_notes):
        flag = input("Уверены что хотите удалить? (да/нет):").strip().lower()
        if flag == "да":
            print("Удаление успешно завершено!")
            return res
        else:
            return list_notes
    else:
        print("Заметок с таким именем пользователя или заголовком не найдено")
        return list_notes

@print_
def delete_note_by_number(list_notes, number):
    if not list_notes:
        print("Список заметок пуст!")
        return list_notes

    res = list_notes.copy()

    try:
        flag = input("Уверены что хотите удалить? (да/нет):").strip().lower()
        if flag == "да":
            res.pop(number)
            print("Удаление успешно завершено!")
        return res
    except IndexError:
        print("Неверный номер, повторите попытку!")
    return res

lst = list(generate_notes(5))

def delete_note(list_notes):
    if not list_notes:
        print("Список пустой!\n")
        return list_notes

    while True:
        try:
            flag = int(input("Выберите пункт (укажите число):"
                             "\n1. Удалить все заметки по имени пользователя или названию заголовка"
                             "\n2. Удалить по номеру"
                             "\n3. Показать текущие заметки"
                             "\n4. Завершить\n").strip())
            if flag == 4:
                break
            elif flag not in (1, 2, 3):
                print("Неверный пункт")
                continue
            elif flag == 1:
                name = input("Введите имя или заголовок: ").strip()
                list_notes = delete_notes_by_criteria(list_notes, name)
            elif flag == 2:
                n = int(input("Укажите номер заметки: ").strip().lower())
                list_notes = delete_note_by_number(lst, n - 1)
            else:
                display_notes(list_notes)
        except ValueError:
            print("Неверный формат, повторите попытку")


if __name__ == '__main__':
    delete_note(lst)
