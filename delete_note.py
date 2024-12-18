from multiple_notes import date_now, display_notes, MESSAGE
from datetime import timedelta
import random

names = ["Богдан", "Антон", "Настя", "Роман", "Анатолий", "Евгений", "Катя", "Леша"]
titles = ["Список покупок", "Подготовка к экзамену", "Посетить вебинар", "Сделать ДЗ", "Приготовить ужин", "Встреча с заказчиком"]
statuses = ["новая", "в процессе", "выполнено"]
lst = []

for i in range(5):
    n = random.randint(0, len(names) - 1)
    t = random.randint(0, len(titles) - 1)
    s = random.randint(0, len(statuses) - 1)
    day = random.randint(0, 15)
    d = {
        "name": names[n],
        "title": titles[t],
        "content": "",
        "status": statuses[s],
        "created_date": date_now,
        "issue_date": date_now + timedelta(days=day)
    }
    lst.append(d)



def del_note(list_notes, key, val):
    res = list(filter(lambda x: x.get(key).strip().lower() != val.lower(), list_notes))
    if len(res) != len(list_notes):
        print("="*10)
        print("Удаление успешно завершено!")
        print("=" * 10)
        return res
    else:
        print("=" * 10)
        print("Заметок с таким именем пользователя не найдено") if key == "name" else (
            print("Заметок с таким заголовком не найдено"))
        print("=" * 10)
        return list_notes


while True:
    try:
        flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Удалить заметку по имени пользователя"
                         "\n2. Удалить заметку по имени названию заголовка"
                         "\n3. Показать текущие заметки"
                         "\n4. Завершить\n").strip())
        if not (1 <= flag <= 4):
            print("Неверный пункт")
            continue
        elif flag == 1:
            name = input("Введите имя: ").strip()
            lst = del_note(lst, "name", name)
        elif flag == 2:
            title = input("Введите заголовок: ").strip()
            lst = del_note(lst, "title", title)
        elif flag == 3 and "lst" in locals():
            display_notes(lst)
        else:
            break
    except ValueError:
        print(MESSAGE)

