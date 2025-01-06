def save_notes_to_file(notes, filename):
    from datetime import datetime as dt
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
                file.write(f"  Дата создания: {note.get("created_date").strftime("%d-%m-%Y")}\n")
                file.write(f"  Дедлайн: {note.get("issue_date").strftime("%d-%m-%Y")}\n")
                file.write("\n")
    except FileExistsError:
        print("Файл с таким именем уже существует!")

def main():
    from Data import generate_notes, date_now
    notes = list(generate_notes(5))
    file_name = "notes_" + date_now.strftime("%d_%m_%Y") + ".yaml"
    save_notes_to_file(notes, file_name)

if __name__ == '__main__':
    main()