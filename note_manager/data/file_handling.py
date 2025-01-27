import datetime
from datetime import datetime as dt
import json
import yaml


def save_notes_to_file(notes, filename):
    if not notes:
        raise ValueError("Список пуст")
    # try:
    with open(filename, 'w', encoding='utf-8') as file:
        for note in notes:
            file.write(f"- id: {note.get("id")}\n")
            file.write(f"  username: {note.get("username")}\n")
            file.write(f"  title: {note.get("title")}\n")
            file.write(f"  content: {note.get("content")}\n")
            file.write(f"  status: {note.get("status")}\n")
            created_date = note.get("created_date")
            issue_date = note.get("issue_date")
            if isinstance(created_date, datetime.date):
                created_date = created_date.strftime("%d-%m-%Y")
            if isinstance(issue_date, datetime.date):
                issue_date = issue_date.strftime("%d-%m-%Y")
            file.write(f"  created_date: {created_date}\n")
            file.write(f"  issue_date: {issue_date}\n")
            file.write("\n")
    # except Exception as e:
    #     print(f"Что-то пошло не так\n{e}")

def load_notes_from_file(filename):
    from datetime import datetime as dt
    notes = []
    # try:
    with open(filename, encoding='utf-8') as file:
        line = file.readline()

        while line:
            note = {}
            while line:
                key = line.split(":")[0].strip().replace("- ", "")
                val = line.split(":")[1].strip()
                # if key in ("created_date", "issue_date"):
                #     val = dt.strptime(val, "%d-%m-%Y").date()
                # if key == "id":
                #     val = int(val)
                note.setdefault(key, val)
                line = file.readline().strip()
            notes.append(note)
            line = file.readline()
    # except FileNotFoundError:
    #     with open(filename, 'w', encoding='utf-8') as file:
    #         print(f"Файл {filename} не найден. Создан новый файл.")
    # finally:
    return notes

def append_notes_to_file(notes, filename):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            for note in notes:
                file.write(f"- Имя пользователя: {note.get("username")}\n")
                file.write(f"  Заголовок: {note.get("title")}\n")
                file.write(f"  Описание: {note.get("content")}\n")
                file.write(f"  Статус: {note.get("status")}\n")
                created_date = note.get("created_date")
                issue_date = note.get("issue_date")
                if isinstance(created_date, datetime.date):
                    created_date = created_date.strftime("%d-%m-%Y")
                if isinstance(issue_date, datetime.date):
                    issue_date = issue_date.strftime("%d-%m-%Y")
                file.write(f"  Дата создания: {created_date}\n")
                file.write(f"  Дедлайн: {issue_date}\n")
                file.write("\n")
    except Exception as e:
        print(f"Ошибка {e}")

def append_notes_to_json(notes, filename):
    if not notes:
        raise ValueError("Список пуст")
    with open(filename, "a", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False, default=serializer)

def serializer(obj):
    if isinstance(obj, datetime.date):
        return obj.strftime("%d-%m-%Y")
    raise TypeError

def deserializer(object_):
    obj = object_.copy()
    created_date = obj.get("created_date")
    issue_date = obj.get("issue_date")


    created_date = dt.strptime(created_date, "%d-%m-%Y").date()
    issue_date = dt.strptime(issue_date, "%d-%m-%Y").date()

    obj.update({"created_date": created_date})
    obj.update({"issue_date": issue_date})
    return obj

def save_notes_json(notes, filename):
    if not notes:
        raise ValueError("Список пуст")
    with open(filename+".json", 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4, ensure_ascii=False, default=serializer)

def load_notes_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        notes = json.load(file, object_hook=deserializer)
        return notes

def save_notes_yaml(notes, filename):
    with open(filename + ".yaml", "w", encoding="utf-8") as file:
        yaml.dump(notes, file, sort_keys=False, allow_unicode=True, encoding="utf-8")