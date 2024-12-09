from datetime import datetime as dt

data = {}

user = input("Ведите ваше имя: ").strip()
title = input("Введите заголовок заметки: ").strip()
content = input("Введите описание заметки: ").strip()
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ").strip()
issue_date = input("Введите дату окончания заметки в формате 'день-месяц-год': ").strip()

created_date = dt.strptime(created_date, "%d-%m-%Y")
issue_date = dt.strptime(issue_date, "%d-%m-%Y")
date_now = dt.now()

data[user] = {
    "title": title,
    "content": content,
    "created_date": created_date,
    "issue_date": issue_date,
    "status": date_now < issue_date
}

print(f"Имя: {user}")
print(f"Заметка: {data[user]['title']}")
print(f"Описание заметки: {data[user]['content']}")
print(f"Дата создания заметки: {data[user]['created_date'].date()}")
print(f"Дата истечения времени заметки: {data[user]['issue_date'].date()}")
print(f"Статус заметки: {data[user]['status']}")

