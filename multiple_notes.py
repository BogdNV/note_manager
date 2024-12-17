from datetime import datetime as dt
date_now = dt.now().date()
notes = []

MESSAGE = "Неверный формат, повторите попытку"

#функция для запроса даты дедлайна
def get_date(format):
    while True:
        try:
            date = input("Введите дедлайн (день-месяц-год): ").strip()
            date = dt.strptime(date, format).date()
            return date
        except:
            print(MESSAGE)

#функция для запроса статуса у пользователя
def get_status():
    statuses = ["новая", "в процессе", "выполнено"]
    while True:
        try:
            n = int(input("Введите статус заметки (укажите число):\n1.новая\n2.в процессе\n3.выполнено\n").strip())
            if 1 <= n <= len(statuses) - 1:
                return statuses[n - 1]
            else:
                print("Вы ввели неверное число!")

        except:
            print(MESSAGE)

#выводит на экран список заметок
def display_notes(notes):
    if notes:
        print("\nСписок заметок:")
        for i, note in enumerate(notes):
            print(f"{i+1}. Имя: {note['user']}")
            print((" "*len(f"{i+1}. ")) + f"Заголовок: {note["title"]}")
            print((" "*len(f"{i+1}. ")) + f"Описание: {note["content"]}")
            print((" "*len(f"{i+1}. ")) + f"Статус: {note["status"]}")
            print((" "*len(f"{i+1}. ")) + f"Дата создания: {note["created_date"].strftime("%d-%m-%Y")}")
            print((" "*len(f"{i+1}. ")) + f"Дедлайн: {note["issue_date"].strftime("%d-%m-%Y")}")
            print()
    else:
        print("\nСписок заметок пуст.")

def check_note(dict_list, name, title):
    for d in dict_list:
        if d.get("name") == name and d.get("content") == title:
            return True
    return False

def get_name_title():
    name = input("Введите имя пользователя: ").strip()
    while not name:
        print("Имя не может быть пустым.")
        name = input("Введите имя пользователя: ").strip()

    title = input("Введите заголовок заметки: ").strip()
    while not title:
        print("Заголовок не может быть пустым.")
        title = input("Введите заголовок заметки: ").strip()
    return name, title

#запрашивает у пользователя данные для заметки и формирует словарь
def get_note():
    global date_now
    global notes

    note = {}
    name, title = get_name_title()
    if not check_note(notes, name, title):
        print("Такая заметка уже существует")
        return

    content = input("Введите описание заголовка: ").strip()
    status = get_status()
    issue_date = get_date("%d-%m-%Y")
    note["name"] = name
    note["title"] = title
    note["content"] = content
    note["status"] = status
    note["created_date"] = date_now
    note["issue_date"] = issue_date
    return note


print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")

while True:
    note = get_note()
    if note:
        notes.append(note)

    flag = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
    if flag == "нет":
        break

display_notes(notes)