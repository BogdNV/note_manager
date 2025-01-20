import tkinter as tk
from tkinter import messagebox, ttk
import datetime
from datetime import datetime as dt, timedelta

from utils import _statuses, validate_name_title, validate_date, validate_note
from interface import create_note, search_notes
from tests import generate_notes

date_now = dt.now().date()

class NoteManager():
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        if not validate_note(self.notes, note):
            raise ValueError("Заметка с таким пользователем уже существует")
        if isinstance(note, dict):
            self.notes.append(note)
        elif isinstance(note, list):
            self.notes.extend(note)


    def get_notes(self, keyword=None, status=None):
        return search_notes(self.notes, keyword=keyword, status=status)


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

        
class BaseFrame(tk.Frame):
    _nm = NoteManager()
    def __init__(self, master):
        super().__init__(master)
        if self.__class__.__name__ == "StartFrame":
            back_btn = ttk.Button(self, text="Завершить программу", command=self.exit_program, width=30)
        else:
            back_btn = ttk.Button(self, text="Вернуться в предыдущее меню", command=master.go_back, width=30)
        back_btn.pack(side="bottom", pady=40)

        self.tree = None
        self.scrollbar = None

    def exit_program(self):
        """Подтверждение выхода из программы"""
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.master.destroy()

    def create_tree(self, list_notes):
        columns = {
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
            if isinstance(note["created_date"], datetime.date):
                note["created_date"] = note["created_date"].strftime("%d-%m-%Y")
            if isinstance(note["issue_date"], datetime.date):
                note["issue_date"] = note["issue_date"].strftime("%d-%m-%Y")
            self.tree.insert("", tk.END, values=tuple(note.values()))

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def configure_tree_columns(self, columns):
        for col in columns:
            self.tree.heading(col, text=columns[col], anchor=tk.W, command=lambda c=col: self.sort_column(c))
            self.tree.column(col, width=110)

    def sort_column(self, col, reverse=False):
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children()]

        data.sort(key=lambda x: x[0], reverse=reverse)

        for i, (_, child) in enumerate(data):
            self.tree.move(child, "", i)

        self.tree.heading(col, command=lambda : self.sort_column(col, not reverse))


    def create_buttom(self, text, command, width=30, pady=6, side="top"):
        but = ttk.Button(self, text=text, command=command, width=width)
        but.pack(pady=pady, side=side)
        return but

class StartFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        create_note_btn = self.create_buttom("Создать новую заметку", lambda: master.show_frame(CreateNoteFrame))
        display_notes_btn = self.create_buttom("Показать текущие заметки", lambda: master.show_frame(DisplayNotesFrame))
        update_note_btn = self.create_buttom("Обновить текущие заметки", lambda: master.show_frame(UpdateNoteFrame))
        delete_note_btn = self.create_buttom("Удалить заметку", lambda: master.show_frame(DeleteNoteFrame))
        search_notes_btn = self.create_buttom("Поиск заметок", lambda: master.show_frame(SearchNoteFrame))
        create_test_notes = self.create_buttom("Создать тестовые заметки", command=self.create_notes, side="bottom")

    def create_notes(self):
        nt = list(generate_notes(10))
        try:
            for note in nt:
                self._nm.add_note(note)
        except:
            pass


class CreateNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        self._message = "Окно для создания заметки"
        master.message_label.set(self._message)
        self.entries = []
        self.select_status = tk.StringVar(value=_statuses[0])

        messages = ["Введите имя", "Введите заголовок", "Введите описание",
                    "Выберите статус",
                    "Ведите дату дедлайна в формате 'дд-мм-гггг' (или оставте пустым)"]

        for i, msg in enumerate(messages):
            label = ttk.Label(self, text=msg)
            label.pack()
            # label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

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
        self._message = "Окно для отображения заметок"
        master.message_label.set(self._message)

        self.create_tree(self._nm.notes)



class UpdateNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        self._message = "Окно для обновления заметок"
        master.message_label.set(self._message)

class DeleteNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        self._message = "Окно для удаления заметок"
        master.message_label.set(self._message)


class SearchNoteFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        self._message = "Окно для поиска заметок"
        master.message_label.set(self._message)

        self.new = tk.IntVar()
        self.done = tk.IntVar()
        self.in_progress = tk.IntVar()

        label = ttk.Label(self, text="Введите имя пользователя или заголовок")
        label.pack()

        self.entry = ttk.Entry(self)
        self.entry.pack()

        self.new_checkbut = ttk.Checkbutton(self, text="новая", variable=self.new)
        self.new_checkbut.pack()

        self.in_progress_checkbut = ttk.Checkbutton(self, text="в процессе", variable=self.in_progress)
        self.in_progress_checkbut.pack()

        self.done_checkbut = ttk.Checkbutton(self, text="выполнено", variable=self.done)
        self.done_checkbut.pack()


        but = ttk.Button(self, text="Найти", command=self.click)
        but.pack()

    def click(self):
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