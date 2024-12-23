from Data import date_now
from datetime import datetime, timedelta
from display_notes_function import display_notes

#функция для запроса даты дедлайна
def get_date(format):
    while True:
        try:
            date = input("Введите дедлайн (день-месяц-год) или оставьте пустым чтобы создать по умолчанию:"
                         "\nпо умолчанию - через неделю от текущей даты\n").strip()
            if date:
                date = datetime.strptime(date, format).date()
            else:
                date = date_now + timedelta(days=7)
            return date
        except:
            print("Неверный формат, повторите попытку")

#функция для запроса статуса у пользователя
def get_status():
    statuses = ["новая", "в процессе", "выполнено"]
    while True:
        try:
            n = int(input("Введите статус заметки (укажите число):"
                          "\n1.новая"
                          "\n2.в процессе"
                          "\n3.выполнено\n").strip())
            return statuses[n - 1]
        except ValueError:
            print("Неверный формат, повторите попытку")
        except IndexError:
            print("Вы ввели неверное число!")



#запрашивает у пользователся имя и заголовок заметки
def get_name_title():
    name = input("Введите имя пользователя: ").strip()
    while not name:
        print("Имя не может быть пустым.")
        name = input("Введите имя пользователя: ").strip()

    title = input("Введите заголовок заметки: ").strip()
    while not title:
        print("Заголовок не может быть пустым.")
        title = input("Введите заголовок заметки: ").strip()
    return name.capitalize(), title[0].upper() + title[1:]

#запрашивает у пользователя данные для заметки и формирует словарь
def create_note():
    note = {}
    name, title = get_name_title()

    content = input("Введите описание заголовка: ").strip()
    if not content:
        print("Описание оставлено пустым.")

    status = get_status()
    issue_date = get_date("%d-%m-%Y")

    note["username"] = name
    note["title"] = title
    note["content"] = content
    note["status"] = status
    note["created_date"] = date_now
    note["issue_date"] = issue_date

    return note

if __name__ == '__main__':
    display_notes([create_note()])