from datetime import timedelta
from multiple_notes import date_now
import random

names = ["Богдан", "Антон", "Настя", "Роман", "Анатолий", "Евгений", "Катя", "Леша"]
titles = ["Список покупок", "Подготовка к экзамену", "Посетить вебинар", "Сделать ДЗ", "Приготовить ужин", "Встреча с заказчиком"]
statuses = ["новая", "в процессе", "выполнено"]

def generate_notes(cnt):
    for i in range(cnt):
        day = random.randint(1, 15)
        d = {}
        d.setdefault("id", id(d))
        d.setdefault("username", random.choice(names))
        d.setdefault("title", random.choice(titles))
        d.setdefault("content", "")
        d.setdefault("status", random.choice(statuses))
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