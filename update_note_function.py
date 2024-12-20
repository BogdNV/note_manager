import datetime
from Data import generate_notes
from multiple_notes import get_date

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

    flag = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date) "
                 "(stop, стоп) для отмены: ").strip().lower()

    while flag not in note or flag == "created_date":
        if flag in ("stop", "стоп"):
            print("Обновление отменено.")
            return
        flag = input("Неверный формат, повторите попытку!: ").strip().lower()

    if flag == "issue_date":
        data = get_date("%d-%m-%Y")
        note.update({flag:data})

    elif flag == "status":
        statuses = ["новая", "в процессе", "выполнено"]
        current_status = note.get(flag, "")

        while True:
            input_string = "Выберите значение из списка:\n"

            for i, s in enumerate(statuses, start=1):
                if s != current_status:
                    input_string += f"{i}. {s}\n"

            status_input = input(input_string).strip()

            try:
                status_index = int(status_input) - 1
                note.update({flag:statuses[status_index]})
                break
            except ValueError:
                print("Неверный формат. Введите номер статуса.")
            except IndexError:
                print("Неверный номер, повторите попытку!")

    else:
        val = input("Введите новое значение: ").strip().lower()
        note.update({flag:val.capitalize()})

    print("\nОбновление успешно завершено!\n")
    print("Обновленные данные заметки:")
    print_note(note)

update_note(lst[0])