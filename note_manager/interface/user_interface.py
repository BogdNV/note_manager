from datetime import datetime, timedelta
from note_manager.utils import _statuses, validate_date


def  search_notes(notes, keyword=None, status=None):
    if keyword and status:
        keyword = keyword.lower()
        return [
            note for note in notes
            if (any(keyword in note[key].lower() for key in ("username", "title", "content")))
            and (note.get("status").lower() in status)
        ]
    if keyword:
        keyword = keyword.lower()
        return [
            note for note in notes
            if (any(keyword in note[key].lower() for key in ("username", "title", "content")))
        ]
    if status:
        return [
            note for note in notes
            if (note.get("status").lower() in status)
        ]
    return notes

#запрашивает у пользователя данные для заметки и формирует словарь
def create_note(name, title, content, status, created_date, issue_date, id_note=None):
    note = {}

    note["id"] = id_note
    note["username"] = name.strip().capitalize()
    note["title"] = title[0].upper() + title[1:]
    note["content"] = content.strip()
    note["status"] = status
    note["created_date"] = created_date
    note["issue_date"] = issue_date

    return note
