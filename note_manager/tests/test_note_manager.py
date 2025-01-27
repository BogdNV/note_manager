import unittest
import random
from datetime import datetime as dt, timedelta
from note_manager.data import save_notes_json, load_notes_from_file, save_notes_to_file, load_notes_json
from note_manager.interface import create_note


date_now = dt.now().date()

names = ["Богдан", "Антон", "Настя", "Роман", "Анатолий", "Евгений", "Катя", "Леша"]
titles = ["Список покупок", "Подготовка к экзамену", "Посетить вебинар", "Сделать ДЗ", "Приготовить ужин", "Встреча с заказчиком"]
statuses = ["новая", "в процессе", "выполнено"]


def generate_notes(cnt):
    for i in range(cnt):
        day = random.randint(1, 15)
        name = random.choice(names)
        title = random.choice(titles)
        status = random.choice(statuses)
        created_date = date_now
        issue_date = date_now + timedelta(days=day)
        d = create_note(name, title, "", status, created_date, issue_date)
        yield d

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = list(generate_notes(5))
        # save_notes_to_file(notes, "test.yaml")
        # loaded_notes = load_notes_from_file('test.yaml')
        save_notes_json(notes, 'test')
        loaded_notes = load_notes_json('test.json')
        self.assertEqual(notes, loaded_notes)



if __name__ == '__main__':

    unittest.main()