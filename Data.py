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
        day = random.randint(1, 15)
        d = {}
        d.setdefault("id", id(d))
        d.setdefault("name", names[n])
        d.setdefault("title", titles[t])
        d.setdefault("content", "")
        d.setdefault("status", statuses[s])
        d.setdefault("created_date", date_now)
        d.setdefault("issue_date", date_now + timedelta(days=day))
        yield d

def print_(func):
    def wrapper(*args, **kwg):
        print('-'*20)
        if args:
            res = func(*args)
            print('-'*20)
            return res
        if kwg:
            res = func(**kwg)
            print('-'*20)
            return res
    return wrapper