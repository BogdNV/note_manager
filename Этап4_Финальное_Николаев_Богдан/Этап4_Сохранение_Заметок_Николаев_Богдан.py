

def save_notes_to_file(notes, filename):
    import datetime
    if not notes:
        print("Список пуст")
        return
    try:
        with open(filename, 'w', encoding='utf-8') as file:
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
        print(f"Что-то пошло не так\n{e}")

def main():
    from Data import generate_notes, date_now
    notes = list(generate_notes(5))
    file_name = "notes_" + date_now.strftime("%d_%m_%Y") + ".yaml"
    save_notes_to_file(notes, file_name)

if __name__ == '__main__':
    main()