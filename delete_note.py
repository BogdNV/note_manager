from multiple_notes import display_notes, MESSAGE
from Data import generate_notes


def del_note(list_notes, key, val):
    res = list(filter(lambda x: x.get(key).strip().lower() != val.lower(), list_notes))
    if len(res) != len(list_notes):
        print("="*10)
        print("Удаление успешно завершено!")
        print("=" * 10)
        return res
    else:
        print("=" * 10)
        print("Заметок с таким именем пользователя не найдено") if key == "name" else (
            print("Заметок с таким заголовком не найдено"))
        print("=" * 10)
        return list_notes

lst = list(generate_notes(5))

while True:
    try:
        flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Удалить заметку по имени пользователя"
                         "\n2. Удалить заметку по имени названию заголовка"
                         "\n3. Показать текущие заметки"
                         "\n4. Завершить\n").strip())
        if not (1 <= flag <= 4):
            print("Неверный пункт")
            continue
        elif flag == 1:
            name = input("Введите имя: ").strip()
            lst = del_note(lst, "name", name)
        elif flag == 2:
            title = input("Введите заголовок: ").strip()
            lst = del_note(lst, "title", title)
        elif flag == 3 and "lst" in locals():
            display_notes(lst)
        else:
            break
    except ValueError:
        print(MESSAGE)

