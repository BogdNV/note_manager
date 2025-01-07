from Этап4_Загрузка_Заметок_Николаев_Богдан import load_notes_from_file
from display_notes_function import display_notes


filename = "notes_07_01_2025.yaml"


try:
    notes = load_notes_from_file(filename)
    display_notes(notes)
except UnicodeDecodeError:
    print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое")
except PermissionError:
    print("Ошибка доступа")
except Exception as e:
    print(f"Ошибка {e}")