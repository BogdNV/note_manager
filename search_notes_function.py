from display_notes_function import display_notes
from Data import generate_notes, check_imported
from create_note_function import get_status


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
    return notes

def handle_choice(choice, notes):
    keyword = None
    status = None
    if choice == 1:
        keyword = input("Введите критерий: ").strip().lower()
    elif choice == 2:
        status = get_status()
    elif choice == 3:
        keyword = input("Введите критерий: ").strip().lower()
        status = get_status()
    return search_notes(notes, keyword=keyword, status=status)


lst = tuple(generate_notes(10))

@check_imported
def run_search_notes(notes, **kwargs):
    exit_message = "Вернуться в предыдущее меню" if kwargs.get("imported", False) else "Завершить"

    while True:
        try:
            flag = int(input(f"Выберите пункт (укажите число):"
                             "\n1. Поиск по ключевому слову"
                             "\n2. Поиск по статусу"
                             "\n3. Поиск по ключевому слову и статусу"
                             "\n4. Показать текущие заметки"
                             f"\n5. {exit_message}\n").strip())
            if flag == 5:
                break
            elif flag not in (1, 2, 3, 4):
                print("Неверный пункт")
                continue
            display_notes(handle_choice(flag, notes))
        except ValueError:
            print("Неверный формат, повторите попытку")


if __name__ == '__main__':
    run_search_notes(lst, imported=False)