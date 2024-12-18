from datetime import timedelta
from multiple_notes import date_now
import random

names = ["Богдан", "Антон", "Настя", "Роман", "Анатолий", "Евгений", "Катя", "Леша"]
titles = ["Список покупок", "Подготовка к экзамену", "Посетить вебинар", "Сделать ДЗ", "Приготовить ужин", "Встреча с заказчиком"]
statuses = ["новая", "в процессе", "выполнено"]

def generate_notes(cnt):
    for i in range(cnt):
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
        yield d