from create_note_function import create_note
from display_notes_function import display_notes
from delete_note import delete_note
from update_note_function import update_note
from search_notes_function import run_search_notes

notes = []

while True:
    try:
        flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Создать новую заметку"
                         "\n2. Показать все заметки"
                         "\n3. Обновить заметку"
                         "\n4. Удалить заметку"
                         "\n5. Найти заметки"
                         "\n6. Завершить\n").strip())
        if flag == 6:
            break
        elif flag == 1:
            note = create_note()
            notes.append(note)
            print("Заметка успешно создана")
        elif flag == 2:
            display_notes(notes)
        elif flag == 3:
            display_notes(notes)
            n = int(input("Укажите номер заметки: "))
            update_note(notes[n-1])
        elif flag == 4:
            delete_note(notes)
        else:
            res = run_search_notes(notes)
            display_notes(res)
    except ValueError:
        print("Неверный формат, повторите попытку")
    except IndexError:
        print("Неверный пункт, повторите попытку")