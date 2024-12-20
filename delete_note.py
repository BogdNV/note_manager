from multiple_notes import display_notes, MESSAGE
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
def delete_note_by_number(notes, number):
    try:
        number = int(number)
        if number < len(notes):
            flag = input("Уверены что хотите удалить? (да/нет):").strip().lower()
            if flag == "да":
                notes.pop(number)
                print("Удаление успешно завершено!")
        return notes
    except ValueError:
        print(MESSAGE)
    except IndexError:
        print("Неверный номер, повторите попытку!")
    return notes

lst = list(generate_notes(5))

while True:
    try:
        flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Удалить все заметки по имени пользователя или названию заголовка"
                         "\n2. Удалить по номеру"
                         "\n3. Показать текущие заметки"
                         "\n4. Завершить\n").strip())
        if not (1 <= flag <= 4):
            print("Неверный пункт")
            continue
        elif flag == 1:
            name = input("Введите имя или заголовок: ").strip()
            lst = delete_notes_by_criteria(lst, name)
        elif flag == 2:
            n = int(input("Укажите номер заметки: ").strip().lower())
            lst = delete_note_by_number(lst, n-1)
        elif flag == 3 and "lst" in locals():
            display_notes(lst)
        else:
            break
    except ValueError:
        print(MESSAGE)
    except IndexError:
        print("Неверный номер, повторите попытку!")


