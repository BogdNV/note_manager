import sqlite3 as sq
import datetime

from greetings import username, title

with sq.connect("notes.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status TEXT NOT NULL,
    created_date TEXT NOT NULL,
    issue_date TEXT NOT NULL
    )""")

def save_note_to_db(note, db_path):
    username = note.get("username")
    title = note.get("title")
    content = note.get("content")
    status = note.get("status")
    created_date = note.get("created_date")
    issue_date = note.get("issue_date")
    if isinstance(created_date, datetime.date):
        created_date = created_date.strftime("%d-%m-%Y")
    if isinstance(issue_date, datetime.date):
        issue_date = issue_date.strftime("%d-%m-%Y")
    with sq.connect(db_path) as con:
        cur = con.cursor()

        cur.execute("""INSERT INTO notes (username, title, content, status, created_date, issue_date) 
        VALUES (?, ?, ?, ?, ?, ?)""", (username, title, content, status, created_date, issue_date))

        con.commit()

def load_notes_from_db(db_path):
    notes = []
    with sq.connect(db_path) as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM notes;")
        res = cur.fetchall()
        for n in res:
            note = {}
            note.setdefault("id", n[0])
            note.setdefault("username", n[1])
            note.setdefault("title", n[2])
            note.setdefault("content", n[3])
            note.setdefault("status", n[4])
            note.setdefault("created_date", n[5])
            note.setdefault("issue_date", n[6])

            notes.append(note)


    return notes

if __name__ == '__main__':
    # save_note_to_db({
    #     "username": "Богдан",
    #     "title": "Сделать ДЗ",
    #     "content":"",
    #     "status": "новая",
    #     "created_date":"27-01-2025",
    #     "issue_date":"31-01-2025"
    # }, "notes.db")

    print(load_notes_from_db("notes.db"))