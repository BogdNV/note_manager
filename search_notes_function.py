from display_notes_function import display_notes
from Data import generate_notes


def  search_notes(notes, keyword=None, status=None):
    if keyword and status:
        return [
            note for note in notes
            if (any(keyword in note[key].lower() for key in ("username", "title", "content")))
            and (note.get("status").lower() == status)
        ]
    if keyword:
        return [
            note for note in notes
            if (any(keyword in note[key].lower() for key in ("username", "title", "content")))
        ]
    if status:
        return [
            note for note in notes
            if (note.get("status").lower() == status)
        ]

lst = tuple(generate_notes(10))

# display_notes(search_notes(lst, "антон"))

while True:
    try:
        flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Поиск по ключевому слову"
                         "\n2. Поиск по статусу"
                         "\n3. Поиск по ключевому слову и статусу"
                         "\n4. Показать текущие заметки"
                         "\n5. Завершить\n").strip())
        if flag == 5:
            break
        elif flag not in (1, 2, 3, 4):
            print("Неверный пункт")
            continue
        elif flag == 1:
            keyword = input("Введите критрий: ").strip().lower()
            display_notes(search_notes(lst, keyword=keyword))
        elif flag == 2:
            status = input("Введите статус: ").strip().lower()
            display_notes(search_notes(lst, status=status))
        elif flag == 3:
            keyword = input("Введите критрий: ").strip().lower()
            status = input("Введите статус: ").strip().lower()
            display_notes(search_notes(lst, keyword=keyword, status=status))
        else:
            display_notes(lst)
    except ValueError as e:
        print(e)
