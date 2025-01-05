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
    except PermissionError:
        print("Отсутсвие прав доступа")
    finally:
        return notes