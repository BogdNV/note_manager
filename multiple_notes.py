from datetime import datetime as dt
date_now = dt.now().date()

MESSAGE = "Неверный формат, повторите попытку"

#функция для запроса даты дедлайна
def get_date(format):
    while True:
        try:
            date_string = input("Введите дедлайн (день-месяц-год): ").strip()
            date_string = dt.strptime(date_string, format).date()
            return date_string
        except:
            print(MESSAGE)

#функция для запроса статуса у пользователя
def get_status():
    statuses = ["новая", "в процессе", "выполнено"]
    while True:
        try:
            n = int(input("Введите статус заметки (укажите число)\n1.новая\n2.в процессе\n3.выполнено\n").strip())
            if 1 <= n <= len(statuses) - 1:
                return statuses[n - 1]
            else:
                print("Вы ввели неверное число!")

        except:
            print(MESSAGE)

#выводит на экран список заметок
def print_notes(notes):
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

#запрашивает у пользователя данные для заметки и формирует словарь
def get_note():
    global date_now

    note = {}
    name = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    content = input("Введите описание заметки: ").strip()
    status = get_status()
    created_date = date_now
    issue_date = get_date("%d-%m-%Y")
    note["user"] = name
    note["title"] = title
    note["content"] = content
    note["status"] = status
    note["created_date"] = created_date
    note["issue_date"] = issue_date
    return note

notes = []
print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")

while True:
    notes.append(get_note())
    flag = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
    if flag == "нет":
        break

print_notes(notes)