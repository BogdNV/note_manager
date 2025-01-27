import os
import yaml
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import datetime
from datetime import datetime as dt, timedelta

from utils import _statuses, validate_name_title, validate_date, validate_note
from interface import create_note, search_notes
from tests import generate_notes
from data import *

date_now = dt.now().date()

class NoteManager:
    def __init__(self):
        self.notes = []
        self.__id = 1
    def __getitem__(self, item):
        return self.notes[item]

    def add_note(self, note):
        if not validate_note(self.notes, note):
            raise ValueError("Заметка с таким пользователем уже существует")
        self.set_id()

        if not note.get("id"):
            note["id"] = self.__id
        self.notes.append(note)
        self.__id += 1


    def get_notes(self, keyword=None, status=None):
        return search_notes(self.notes, keyword=keyword, status=status)

    def find_note(self, name, title):
        for i, n in enumerate(self.notes):
            if n.get("username") == name and n.get("title") == title:
                return i
        return -1

    def set_id(self):
        if self.notes:
            list_id = list(map(lambda x: x["id"], self.notes))
            self.__id = max(list_id) + 1

    def reset_id(self):
        for n in self.notes:
            n["id"] = None


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Добро пожаловать в менеджер заметок")
        self.geometry("731x476+796+359")
        self.resizable(False, False)
        self.current_frame = None
        self.previous_frame = None

        self._message = "Главное меню"
        self.message_label = tk.StringVar(value=self._message)
        self.label = ttk.Label(textvariable=self.message_label)
        self.label.pack()


        self.show_frame(StartFrame)

    def show_frame(self, frame_class, *args, **kwargs):
        """Показать указанное окно"""
        if self.current_frame:
            # Удаляем текущее окно
            self.current_frame.destroy()
        # Сохраняем класс текущего окна как предыдущий
        self.previous_frame = self.current_frame.__class__ if self.current_frame else None
        # Создаем новое окно
        self.current_frame = frame_class(self, *args, **kwargs)
        self.current_frame.pack(expand=True, fill="both")


    def go_back(self):
        """Вернуться к предыдущему окну"""
        if self.previous_frame:
            self.show_frame(self.previous_frame)
            self.message_label.set(self._message)

    def exit_program(self):
        """Подтверждение выхода из программы"""
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.destroy()

        
class BaseFrame(tk.Frame):
    _nm = NoteManager()
    def __init__(self, master):
        super().__init__(master)
        if self.__class__.__name__ == "StartFrame":
            self.back_btn = self.create_buttom(
                text="Завершить программу",
                command=master.exit_program,
                width=30,
                side="bottom",
                pady=40)
        else:
            self.back_btn = self.create_buttom(
                text="Вернуться в предыдущее меню",
                command=master.go_back,
                width=30,
                side="bottom",
                pady=40)
        self.tree = None
        self.scrollbar = None



    def create_tree(self, list_notes):
        """Создание дерева для отображения списка заметок"""
        columns = {
            "id": "id",
            "name":"Имя",
            "title":"Заголовок",
            "content":"Описание",
            "status":"Статус",
            "created_date":"Дата создания",
            "issue_date":"Дата дедлайна"
        }

        if self.tree:
            self.tree.destroy()
        if self.scrollbar:
            self.scrollbar.destroy()

        self.tree = ttk.Treeview(
            self,
            columns=list(columns.keys()),
            show="headings",
            height=15
        )
        self.tree.pack(side=tk.LEFT, padx=6)

        self.configure_tree_columns(columns)

        for note in list_notes:
            n = note.copy()
            if isinstance(n["created_date"], datetime.date):
                n["created_date"] = n["created_date"].strftime("%d-%m-%Y")
            if isinstance(n["issue_date"], datetime.date):
                n["issue_date"] = n["issue_date"].strftime("%d-%m-%Y")
            self.tree.insert("", "end", values=tuple(n.values()))

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.context_menu = self.add_context_menu()

    def add_context_menu(self):
        """Меню при нажатии на правую кнопку мыши по заметке"""
        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="Удалить", command=self.delete_note)
        context_menu.add_command(label="Редактировать", command=self.edit_note)

        self.tree.bind("<Button-3>", self.show_context_menu)
        return context_menu

    def delete_note(self):
        """Удалить выбранную заметку"""
        selected_item = self.tree.selection()
        if selected_item:
            # Получаем данные из выделенной строки
            values = self.tree.item(selected_item, "values")
            name, title = values[1], values[2]

            # Удаляем заметку из списка `notes`
            idx_note = self._nm.find_note(name, title)
            self._nm.notes.pop(idx_note)

            self.update_tree()

            messagebox.showinfo("Успешно", f"Заметка '{name}: {title}' удалена")
        else:
            messagebox.showerror("Ошибка", "Не выбрана заметка для удаления")

    def edit_note(self):
        """Редактировать выбранную заметку"""
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            _, name, title, content, status, _, issue_date = values
            labels = {
                "Имя": name,
                "Заголовок": title,
                "Описание": content,
                "Статус": status,
                "Дата дедлайна": issue_date
            }

            entries = {}

            t = tk.Toplevel(self)
            t.geometry(f"400x300+{self.context_menu_position[0]}+{self.context_menu_position[1]}")
            t.resizable(0, 0)

            select_status = tk.StringVar()

            for i, (k, v) in enumerate(labels.items()):
                n = i
                if k == "Статус":
                    select_status.set(v)
                    fr = ttk.Frame(t)
                    fr.grid(row=i, padx=1, column=0, columnspan=2)
                    ttk.Label(fr, text=k).grid(row=i, column=0, padx=10, pady=5, sticky="e")
                    for j in range(1, len(_statuses)+1):
                        ttk.Radiobutton(
                            fr,
                            text=_statuses[j-1],
                            value=_statuses[j-1],
                            variable=select_status
                        ).grid(row=i, column=j, padx=1, pady=1, sticky="e")
                        n += 1
                else:
                    ttk.Label(t, text=k).grid(row=i, column=0, padx=10, pady=5, sticky="e")
                    entry = ttk.Entry(t)
                    entry.insert(0, v)
                    entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')

                    entries[k] = entry



            def save_new():
                """Сохранить новые данные в выбранную заметку"""
                new_name = entries["Имя"].get()
                new_title = entries["Заголовок"].get()
                new_content = entries["Описание"].get()
                new_status = select_status.get()
                new_issue_date = entries["Дата дедлайна"].get()
                if not new_issue_date:
                    new_issue_date = (date_now + timedelta(days=7))
                elif not validate_date(new_issue_date):
                    raise ValueError("Неверный формат даты")
                new_issue_date = dt.strptime(new_issue_date, "%d-%m-%Y").date()

                if not new_name or not new_title:
                    messagebox.showerror("Ошибка", "Имя и заголовок не могут быть пустыми")
                    return

                self._nm[self._nm.find_note(name, title)].update({
                    "username": new_name,
                    "title": new_title,
                    "content": new_content,
                    "status": new_status,
                    "issue_date": new_issue_date
                })

                self.update_tree()
                t.destroy()
                messagebox.showinfo("Успешно", "Заметка успешно обновлена")

            ttk.Button(t, text="Сохранить", command=save_new).grid(row=len(labels)+3, column=0, columnspan=2,pady=10)

            t.transient(self)  # Привязываем окно к главному
            t.grab_set()  # Блокируем взаимодействие с основным окном
            t.wait_window()  # Ждем закрытия окна

    def update_tree(self):
        """Обновить список заметок"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for note in self._nm:
            issue_date = note["issue_date"]
            if isinstance(issue_date, datetime.date):
                issue_date = issue_date.strftime("%d-%m-%Y")
            self.tree.insert("", "end", values=[
                note["id"],
                note["username"],
                note["title"],
                note["content"],
                note["status"],
                note["created_date"],
                issue_date
            ])

    def show_context_menu(self, event):
        """Показать контекстное меню"""
        # Определяем элемент под курсором
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)  # Выделяем строку
            self.context_menu.post(event.x_root, event.y_root)  # Показываем меню
            self.context_menu_position = (event.x_root, event.y_root) # Задаем позицию меню возле курсора

    def configure_tree_columns(self, columns):
        for col in columns:
            self.tree.heading(col, text=columns[col], anchor=tk.W, command=lambda c=col: self.sort_column(c))
            if col == "id":
                self.tree.column(col, width=20)
            else:
                self.tree.column(col, width=110)

    def sort_column(self, col, reverse=False):
        """Сортировка списка заметок по выбранному столбцу"""
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children()]
        if col in ("created_date", "issue_date"):
            data = list(map(lambda x: (dt.strptime(x[0], '%d-%m-%Y'), x[1]), data))
            data.sort(key=lambda x: x[0], reverse=reverse)
            data = list(map(lambda x: (x[0].strftime('%d-%m-%Y'), x[1]), data))
        elif col == "id":
            data = list(map(lambda x: (int(x[0]), x[1]), data))
            data.sort(key=lambda x: x[0], reverse=reverse)
            data = list(map(lambda x: (str(x[0]), x[1]), data))
        else:
            data.sort(key=lambda x: x[0], reverse=reverse)

        for i, (_, child) in enumerate(data):
            self.tree.move(child, "", i)

        self.tree.heading(col, command=lambda : self.sort_column(col, not reverse))


    def create_buttom(self, text, command, width=30, pady=6, side="top"):
        """Создание и размещение кнопки"""
        but = ttk.Button(self, text=text, command=command, width=width)
        but.pack(pady=pady, side=side)
        return but

class StartFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        create_note_btn = self.create_buttom("Создать новую заметку", lambda: master.show_frame(CreateNoteFrame))
        display_notes_btn = self.create_buttom("Показать текущие заметки", lambda: master.show_frame(DisplayNotesFrame))
        search_notes_btn = self.create_buttom("Поиск заметок", lambda: master.show_frame(SearchNoteFrame))
        save_to_file = self.create_buttom(r"Сохранить/Загрузить заметки", lambda: master.show_frame(SaveNoteFrame))
        create_test_notes = self.create_buttom("Создать тестовые заметки", self.create_notes, side="bottom")


    def create_notes(self):
        nt = list(generate_notes(10))
        try:
            for note in nt:
                self._nm.add_note(note)
        except:
            pass

class SaveNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        master.message_label.set("Окно для работы с файлами")

        ttk.Label(self, text="Введите название файла").pack(pady=10)
        self.entry_to_file = ttk.Entry(self)
        self.entry_to_file.pack()

        self.but_json = self.create_buttom(text="Сохранить в формате JSON", command=self.save_to_file)
        self.but_yaml = self.create_buttom(text="Сохранить в формате YAML", command=lambda: self.save_to_file(format="yaml"))
        self.but_open_file = self.create_buttom(text="Загрузить файл", command=self.open_file)


    def open_file(self):
        """Открытие файла (.json .yaml)"""
        file_path = filedialog.askopenfilename()
        try:
            if file_path.endswith("json"):
                notes = load_notes_json(file_path)
            elif file_path.endswith("yaml"):
                # notes = load_notes_from_file(file_path)
                with open(file_path, encoding="utf-8") as file:
                    notes = yaml.load(file, Loader=yaml.FullLoader)
            else:
                raise FileExistsError("Выбран неверный формат файла")
        except Exception as e:
            messagebox.showerror("Ошибка", f"{e}")
            return
        for n in notes:
            self._nm.add_note(n)

    def save_to_file(self, format="json"):
        """Запись в файл"""
        file_name = self.entry_to_file.get()
        try:
            if format == "json":
                save_notes_json(self._nm.notes, file_name)
            elif format == "yaml":
                save_notes_yaml(self._nm.notes, file_name)

            messagebox.showinfo("Успешно", "Файл успешно сохранён")
        except Exception as e:
            messagebox.showerror("Ошибка", f"{e}")



class CreateNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        master.message_label.set("Окно для создания заметки")
        self.entries = []
        self.select_status = tk.StringVar(value=_statuses[0])

        messages = ["Введите имя", "Введите заголовок", "Введите описание",
                    "Выберите статус",
                    "Ведите дату дедлайна в формате 'дд-мм-гггг' (или оставте пустым)"]

        for i, msg in enumerate(messages):
            label = ttk.Label(self, text=msg)
            label.pack()

            if msg.endswith("статус"):
                for st in _statuses:
                    lang_bt = ttk.Radiobutton(self, text=st, value=st, variable=self.select_status)
                    lang_bt.pack(pady=1)
            else:
                entry = ttk.Entry(self)
                entry.pack(pady=1)
                entry.bind("<Return>", self.focus_next_widget)

                self.entries.append(entry)

        self.but = self.create_buttom(text="Добавить заметку", command=self.add_note_to_notes, width=30, pady=6)
        self.but.bind("<Return>", self.add_note_to_notes)

    def add_note_to_notes(self, event=None):
        """Добавляет заметку в список заметок"""
        lst = []
        for entry in self.entries:
            lst.append(entry.get())
            entry.delete(0, tk.END)

        name, title, content, data = lst
        status = self.get_status()
        del lst

        if not data.strip():
            data = (date_now + timedelta(days=7)).strftime("%d-%m-%Y")

        if not self.validate_note_data(name, title, data):
            return

        note = create_note(name, title, content, status, date_now, data)

        try:
            self._nm.add_note(note)
            messagebox.showinfo("Выполнено", "Заметка успешно добавлена")
        except ValueError:
            messagebox.showerror("Ошибка", "Заметка стаким пользователем уже существует!")
            return

    def validate_note_data(self, name, title, data):
        if not validate_name_title(name, title):
            messagebox.showerror("Ошибка", "Имя и заголовок не должны быть пустыми")
            return False
        if not validate_date(data):
            messagebox.showerror("Ошибка", "Неверный формат даты")
            return False
        return True


    def get_status(self):
        """Получение статуса"""
        return self.select_status.get()

    def focus_next_widget(self, event):
        """Переход к следующему виджету"""
        widgets = self.entries + [self.but]
        index = widgets.index(event.widget)  # Определяем текущий индекс
        if index < len(self.entries):
            # Переход к следующему полю
            widgets[index + 1].focus_set()



class DisplayNotesFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        master.message_label.set("Окно для отображения заметок")

        self.create_tree(self._nm)



class SearchNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        master.message_label.set("Окно для поиска заметок")

        self.new = tk.IntVar()
        self.done = tk.IntVar()
        self.in_progress = tk.IntVar()

        label = ttk.Label(self, text="Введите имя пользователя или заголовок")
        label.pack(pady=6)

        self.entry = ttk.Entry(self)
        self.entry.pack()

        self.new_checkbut = ttk.Checkbutton(self, text="новая", variable=self.new)
        self.new_checkbut.pack()

        self.in_progress_checkbut = ttk.Checkbutton(self, text="в процессе", variable=self.in_progress)
        self.in_progress_checkbut.pack()

        self.done_checkbut = ttk.Checkbutton(self, text="выполнено", variable=self.done)
        self.done_checkbut.pack()


        but = ttk.Button(self, text="Найти", command=self.find_notes)
        but.pack()

    def find_notes(self):
        keyword = self.entry.get().strip() if self.entry.get().strip() else None
        self.entry.delete(0, tk.END)
        status = self.select()

        n = self._nm.get_notes(keyword=keyword, status=status)
        self.create_tree(n)


    def select(self):
        status = []
        if self.new.get() == 1: status.append("новая")
        if self.done.get() == 1: status.append("выполнено")
        if self.in_progress.get() == 1: status.append("в процессе")
        return status



if __name__ == '__main__':
    app = App()
    app.mainloop()