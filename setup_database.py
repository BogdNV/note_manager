import sqlite3 as sq
import datetime
from pprint import pprint

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

def update_note_in_db(note_id, updates, db_path):

    with sq.connect(db_path) as con:
        cur = con.cursor()

        cur.execute("""UPDATE notes
        SET title = ?, content = ?, status = ?, issue_date = ?
        WHERE id = ?;""",  (updates['title'], updates['content'], updates['status'], updates['issue_date'], note_id))

        con.commit()

def delete_note_from_db(note_id, db_path):
    with sq.connect(db_path) as con:
        cur = con.cursor()

        cur.execute("DELETE FROM notes WHERE id = ?;", (note_id,))
        con.commit()

def search_notes_by_keyword(keyword, db_path):
    with sq.connect(db_path) as con:
        cur = con.cursor()

        cur.execute("""SELECT *
        FROM notes
        WHERE title LIKE ? OR username LIKE ?""", (f"%{keyword}%", f"%{keyword}%"))
        notes = []
        for row in cur.fetchall():
            notes.append({
                'id': row[0],
                'username': row[1],
                'title': row[2],
                'content': row[3],
                'status': row[4],
                'created_date': row[5],
                'issue_date': row[6]})
        return  notes


if __name__ == '__main__':
    # save_note_to_db({
    #     "username": "Богдан",
    #     "title": "Сделать ДЗ",
    #     "content":"",
    #     "status": "новая",
    #     "created_date":"27-01-2025",
    #     "issue_date":"31-01-2025"
    # }, "notes.db")

    # print(load_notes_from_db("notes.db"))

    # update_note_in_db(1, {
    #     "title": "Сделать ДЗ",
    #     "content": "написать БД",
    #     "status": "выполнено",
    #     "issue_date": "01-02-2025"
    # }, "notes.db")

    # delete_note_from_db(2, "notes.db")
    n = search_notes_by_keyword("Богдан", r"data_base\note_manager.db")

    pprint(n)
    print(len(n))