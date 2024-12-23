from display_notes_function import display_notes
from create_note_function import create_note

notes = []
# MESSAGE = "Неверный формат, повторите попытку"

#проверяет существует ли заметка в списке
def check_note(dict_list, note):
    for d in dict_list:
        if d.get("username") == note.get("username") and d.get("title") == note.get("title"):
            return True
    return False


def main():
    print("Добро пожаловать в \"Менеджер заметок\"!")

    while True:
        try:
            flag = int(input("Выберите пункт (укажите число):"
                         "\n1. Добавить новую заметку"
                         "\n2. Показать текущие заметки"
                         "\n3. Завершить\n").strip())
            if flag == 3:
                break
            elif flag == 1:
                note = create_note()
                if check_note(notes, note):
                    print("Такая заметка уже существует!\n")
                    continue
                notes.append(note)
                print("Заметка упешно добавлена!")
            elif flag == 2:
                display_notes(notes)
            else:
                print("Неверный пункт")
        except ValueError:
            print("Неверный формат, повторите попытку")

if __name__ == "__main__":
    main()

