import datetime
import json


def save_notes_to_file(notes, filename):
    import datetime
    if not notes:
        print("Список пуст")
        return
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                file.write(f"- username: {note.get("username")}\n")
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
    except Exception as e:
        print(f"Что-то пошло не так\n{e}")

def load_notes_from_file(filename):
    from datetime import datetime as dt
    notes = []
    try:
        with open(filename, encoding='utf-8') as file:
            line = file.readline()

            while line:
                note = {}
                while line:
                    key = line.split(":")[0].strip().replace("- ", "")
                    val = line.split(":")[1].strip()
                    if key in ("created_date", "issue_date"):
                        val = dt.strptime(val, "%d-%m-%Y").date()
                    note.setdefault(key, val)
                    line = file.readline().strip()
                notes.append(note)
                line = file.readline()
    except FileNotFoundError:
        with open(filename, 'w', encoding='utf-8') as file:
            print(f"Файл {filename} не найден. Создан новый файл.")
    finally:
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

def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for i in range(len(notes)):
                created_date = notes[i].get("created_date")
                issue_date = notes[i].get("issue_date")

                if isinstance(created_date, datetime.date):
                    created_date = created_date.strftime("%d-%m-%Y")
                if isinstance(issue_date, datetime.date):
                    issue_date = issue_date.strftime("%d-%m-%Y")

                notes[i].update({"created_date": created_date})
                notes[i].update({"issue_date": issue_date})
            json.dump(notes, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка {e}")

def load_notes_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            j_file = json.load(file)
            return j_file
    except:
        print("Не удалось считать файл")