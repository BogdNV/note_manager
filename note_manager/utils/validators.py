from datetime import datetime
import uuid

_statuses = ["новая", "в процессе", "выполнено"]


def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def validate_status(status):
    if status in _statuses:
        return True
    return False

def validate_name_title(name, title):
    if not name.strip() or not title.strip():
        return False
    return True

def validate_note(notes, note):
    for n in notes:
        if note.get("username") == n.get("username") \
            and note.get("title") == n.get("title"):
            return False
    return True


def generate_unique_id():
    return str(uuid.uuid4())