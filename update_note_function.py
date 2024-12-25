import datetime
from Data import generate_notes
from create_note_function import get_date

lst = list(generate_notes(1))


def print_note(note: dict):
    """Функция выводит переданную заметку на экран"""
    for key in note:
        if isinstance(note[key], datetime.date):
            print(f"\t{key}: {note[key].strftime("%d-%m-%Y")}")
        else:
            print(f"\t{key}: {note[key]}")


def update_note(note: dict):
    """Функция обновляет заметку на основе введённых данный с клавиатуры"""
    print("Текущие данные заметки:")
    print_note(note)
    note_keys = ["username", "title", "content", "status", "issue_date"]

    try:
        flag = int(input("Какие данные Вы хотите обновить?:"
                         "\n1. username"
                         "\n2. title"
                         "\n3. content"
                         "\n4. status"
                         "\n5. issue_date"
                         "\n6. Отмена\n").strip())
        while flag not in (1, 2, 3, 4, 5, 6):
            flag = int(input("неверный пункт, повторите попытку!"))
    except ValueError:
        print("Неверный формат, повторите попытку!")

    if flag == 6:
        print("Обновление отменено.")
        return
    elif flag == 5:
        data = get_date("%d-%m-%Y")
        note.update({note_keys[flag-1]:data})

    elif flag == 4:
        statuses = ["новая", "в процессе", "выполнено"]
        current_status = note.get(note_keys[flag-1], "")

        while True:
            input_string = "Выберите значение из списка:\n"

            for i, s in enumerate(statuses, start=1):
                if s != current_status:
                    input_string += f"{i}. {s}\n"

            status_input = input(input_string).strip()

            try:
                status_index = int(status_input) - 1
                note.update({note_keys[flag-1]:statuses[status_index]})
                break
            except ValueError:
                print("Неверный формат. Введите номер статуса.")
            except IndexError:
                print("Неверный номер, повторите попытку!")

    else:
        val = input("Введите новое значение: ").strip().lower()
        note.update({note_keys[flag-1]:val.capitalize()})

    print("\nОбновление успешно завершено!\n")
    print("Обновленные данные заметки:")
    print_note(note)


if __name__ == '__main__':

    update_note(lst[0])