from multiple_notes import get_note, date_now, display_notes, MESSAGE
from datetime import datetime as dt, timedelta
import random


# names = ["Богдан", "Антон", "Андрей", "Роман", "Анатолий", "Евгений"]
# titles = ["Покушать", "Сходить в зал", "пойти на работу", "Сделать ДЗ", "Подстричься", "Запустить бота"]
# statuses = ["новая", "в процессе", "выполнено"]
# lst = []
#
# for i in range(5):
#     n = random.randint(0, len(names)-1)
#     t = random.randint(0, len(titles)-1)
#     s = random.randint(0, len(statuses) - 1)
#     day = random.randint(0, 15)
#     d = {
#         "name": names[n],
#         "title": titles[t],
#         "content": "",
#         "status": statuses[s],
#         "created_date": date_now,
#         "issue_date": date_now + timedelta(days=day)
#     }
#     lst.append(d)

def del_note(list_notes, key, val):
    if list_notes:
        return list(filter(lambda x: x.get(key).strip().lower() != val.lower(), list_notes))
    return []

def main():
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
                name = input("Введите заголовок: ").strip()
                lst = del_note(lst, "title", name)
            elif flag == 3:
                display_notes(lst)
            else:
                break
        except:
            print(MESSAGE)

if __name__ == '__main__':
    main()