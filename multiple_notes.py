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
            n = int(input("Введите статус заметки (укажите число):"
                          "\n1.новая"
                          "\n2.в процессе"
                          "\n3.выполнено\n").strip())
            if not (1 <= n <= len(statuses) - 1):
                print("Вы ввели неверное число!")
            else:
                return statuses[n - 1]
        except:
            print(MESSAGE)


#выводит на экран список заметок
def display_notes(notes):
    if notes:
        print("Список заметок:")
        print("-"*20)
        for i, note in enumerate(notes):
            print(f"{i+1}. Имя: {note.get('username', "")}")
            ind = " "*len(f"{i+1}. ")
            print(ind + f"Заголовок: {note.get("title", "")}")
            print(ind + f"Описание: {note.get("content", "")}")
            print(ind + f"Статус: {note.get("status","")}")
            print(ind + f"Дата создания: {note.get("created_date", date_now).strftime("%d-%m-%Y")}")
            print(ind + f"Дедлайн: {note.get("issue_date", date_now).strftime("%d-%m-%Y")}")
            print("-"*20)
    else:
        print("-" * 20)
        print("Список заметок пуст.")
        print("-" * 20)

#проверяет существует ли заметка в списке
def check_note(dict_list, name, title):
    for d in dict_list:
        if d.get("username", None) == name and d.get("title", None) == title:
            return True
    return False

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
    return name, title

#запрашивает у пользователя данные для заметки и формирует словарь
def get_note():
    global date_now
    global notes

    note = {}
    name, title = get_name_title()
    if check_note(notes, name, title):
        print("Такая заметка уже существует")
        return

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


def main():
    print("Добро пожаловать в \"Менеджер заметок\"!")

    while True:
        try:
            flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Добавить новую заметку"
                         "\n2. Показать текущие заметки"
                         "\n3. Завершить\n").strip())
            if not (1 <= flag <= 3):
                print("Неверный пункт")
                continue
            elif flag == 1:
                note = get_note()
                if note:
                    notes.append(note)
                    print("Заметка упешно добавлена!")
            elif flag == 2:
                display_notes(notes)
            else:
                break
        except ValueError:
            print(MESSAGE)

if __name__ == "__main__":
    main()

