import json
import datetime
from Data import generate_notes

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


def main():
    from Data import generate_notes, date_now
    notes = list(generate_notes(5))
    file_name = "notes_" + date_now.strftime("%d_%m_%Y") + ".json"
    save_notes_json(notes, file_name)


if __name__ == '__main__':
    main()