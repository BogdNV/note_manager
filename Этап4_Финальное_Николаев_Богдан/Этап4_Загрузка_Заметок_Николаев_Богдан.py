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

def main():
    import os
    files = []
    for file_name in os.listdir():
        if file_name.endswith("yaml"):
            files.append(file_name)
    from display_notes_function import display_notes
    if files:
        file_name = files[0]
        notes = load_notes_from_file(file_name)
        display_notes(notes)

if __name__ == '__main__':
    main()