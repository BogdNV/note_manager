def save_notes_to_file(notes, filename):
    from datetime import datetime as dt
    try:
        with open(filename, 'x', encoding='utf-8') as file:
            for note in notes:
                file.write(f"-")
                for key, val in note.items():
                    if key == "username":
                        file.write(f" {key}: {val}\n")
                    elif key in ("created_date", "issue_date"):
                        file.write(f"  {key}: {val.strftime("%d-%m-%Y")}\n")
                    else:
                        file.write(f"  {key}: {val}\n")
                file.write("\n")
    except Exception as e:
        print(e)