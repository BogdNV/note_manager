from Этап4_Загрузка_Заметок_Николаев_Богдан import load_notes_from_file
from Этап4_Сохранение_Заметок_Николаев_Богдан import save_notes_to_file
from Этап4_Добавление_Данных_Николаев_Богдан import append_notes_to_file
from Этап4_JSON_Формат_Николаев_Богдан import save_notes_json
from display_notes_function import display_notes


filename = "notes_07_01_2025.yaml"

def error_handling(func, filename, notes=None):
    try:
        if func is load_notes_from_file:
            notes = func(filename)
            display_notes(notes)
        elif func is save_notes_to_file:
            func(notes, filename)
        elif func is append_notes_to_file:
            func(notes, filename)
        elif func is save_notes_json:
            func(notes, filename)
    except UnicodeDecodeError:
        print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое")
    except PermissionError:
        print("Ошибка доступа")
    except Exception as e:
        print(f"Ошибка {e}")

if __name__ == '__main__':
    error_handling(load_notes_from_file, "notes_10_01_2025.yaml")