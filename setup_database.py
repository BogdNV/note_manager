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
        cur = con.cursor("""INSERT INTO notes (username, title, content, status, created_date, issue_date) 
        VALUES (?, ?, ?, ?, ?, ?)""", username, title, content, status, created_date, issue_date)