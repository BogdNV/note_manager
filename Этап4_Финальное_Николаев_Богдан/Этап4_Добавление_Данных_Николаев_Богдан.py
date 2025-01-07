import datetime
from Data import generate_notes

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

def main():
    notes = generate_notes(3)
    filename = "notes_07_01_2025.yaml"
    append_notes_to_file(notes, filename)

if __name__ == '__main__':
    main()