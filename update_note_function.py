import datetime
from Data import generate_notes
from multiple_notes import get_date

lst = list(generate_notes(1))
def print_note(note):

    for key in note:
        if isinstance(note[key], datetime.date):
            print(f"\t{key}: {note[key].strftime("%d-%m-%Y")}")
        else:
            print(f"\t{key}: {note[key]}")


def update_note(note: dict):
    print("Текущие данные заметки:")
    print_note(note)
    flag = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date): ").strip().lower()
    if flag in ("stop", "стоп"):
        return
    while flag not in note:
        flag = input("Неверный формат, повторите попытку!: ").strip().lower()

    if flag == "issue_date":
        data = get_date("%d-%m-%Y")
        note.update({flag:data})
    else:
        val = input("Введите новое значение: ").strip().lower()
        note.update({flag:val.capitalize()})
    print("\nОбновление успешно завершено!\n")

    print("Обновленные данные заметки:")
    print_note(note)
    # return note

update_note(lst[0])