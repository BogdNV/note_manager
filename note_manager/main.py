import tkinter as tk
from tkinter import messagebox, ttk
import datetime
from datetime import datetime as dt, timedelta

from utils import _statuses, validate_name_title, validate_date, validate_note
from interface import create_note, search_notes
from tests import generate_notes


notes = []
date_now = dt.now().date()



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

    def show_frame(self, frame_class):
        """Показать указанное окно"""
        if self.current_frame:
            # Удаляем текущее окно
            self.current_frame.destroy()
        # Сохраняем класс текущего окна как предыдущий
        self.previous_frame = self.current_frame.__class__ if self.current_frame else None
        # Создаем новое окно
        self.current_frame = frame_class(self)
        self.current_frame.pack(expand=True, fill="both")


    def go_back(self):
        """Вернуться к предыдущему окну"""
        if self.previous_frame:
            self.show_frame(self.previous_frame)
            self.message_label.set(self._message)

        
class BaseFrame(tk.Frame):
    _notes = []
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
        columns = ("name", "title", "content", "status", "created_date", "issue_date")

        if self.tree:
            self.tree.destroy()
        if self.scrollbar:
            self.scrollbar.destroy()

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )
        self.tree.pack(side=tk.LEFT, padx=6)

        self.tree.heading("name", text="Имя", anchor=tk.W, command=lambda: self.sort_column("name"))
        self.tree.heading("title", text="Заголовок", anchor=tk.W, command=lambda: self.sort_column("title"))
        self.tree.heading("content", text="Описание", anchor=tk.W, command=lambda: self.sort_column("content"))
        self.tree.heading("status", text="Статус", anchor=tk.W, command=lambda: self.sort_column("status"))
        self.tree.heading("created_date", text="Дата создания", anchor=tk.W,
                          command=lambda: self.sort_column("created_date"))
        self.tree.heading("issue_date", text="Дата дедлайна", anchor=tk.W,
                          command=lambda: self.sort_column("issue_date"))

        for i, c in enumerate(columns):
            self.tree.column(f"#{i}", width=100)

        for note in list_notes:
            if isinstance(note["created_date"], datetime.date):
                note["created_date"] = note["created_date"].strftime("%d-%m-%Y")
            if isinstance(note["issue_date"], datetime.date):
                note["issue_date"] = note["issue_date"].strftime("%d-%m-%Y")
            self.tree.insert("", tk.END, values=tuple(note.values()))

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def sort_column(self, col, reverse=False):
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children()]

        data.sort(key=lambda x: x[0], reverse=reverse)

        for i, (_, child) in enumerate(data):
            self.tree.move(child, "", i)

        self.tree.heading(col, command=lambda : self.sort_column(col, not reverse))

class StartFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

        # Кнопка "Создать файл"
        create_note_btn = ttk.Button(self, text="Создать новую заметку", width=30,
                                    command=lambda: master.show_frame(CreateNoteFrame))
        create_note_btn.pack(pady=6)


        display_notes_btn = ttk.Button(self, text="Показать текущие заметки", width=30,
                                    command=lambda: master.show_frame(DisplayNotesFrame))
        display_notes_btn.pack(pady=6)


        update_note_btn = ttk.Button(self, text="Обновить заметку", width=30,
                                     command=lambda: master.show_frame(UpdateNoteFrame))
        update_note_btn.pack(pady=6)


        delete_note_btn = ttk.Button(self, text="Удалить заметку", width=30,
                                     command=lambda: master.show_frame(DeleteNoteFrame))
        delete_note_btn.pack(pady=6)


        search_notes_btn = ttk.Button(self, text="Найти заметку", width=30,
                                      command=lambda: master.show_frame(SearchNoteFrame))
        search_notes_btn.pack(pady=6)

        create_test_notes = ttk.Button(self, text="Создать тестовые заметки", width=30,
                                       command=self.create_notes)
        create_test_notes.pack(side="bottom")

    def create_notes(self):
        nt = list(generate_notes(10))
        notes.extend(nt)


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
                    lang_bt.pack(pady=6)
            else:

                entry = ttk.Entry(self)
                entry.pack(pady=6)
                entry.bind("<Return>", self.focus_next_widget)

                self.entries.append(entry)

        self.but = ttk.Button(self, text="Добавить заметку", command=self.add_note_to_notes, width=30)
        self.but.pack()
        self.but.bind("<Return>", self.add_note_to_notes)

    def add_note_to_notes(self, event=None):
        """Добавляет заметку в список заметок"""
        lst = []
        for entry in self.entries:
            lst.append(entry.get())
            entry.delete(0, tk.END)

        status = self.get_status()

        if not validate_name_title(lst[0], lst[1]):
            messagebox.showerror("Ошибка", "Имя и заголовок не должны быть пустыми")
            return

        if not lst[-1].strip():
            lst[-1] = date_now + timedelta(days=7)
        elif validate_date(lst[-1]):
            lst[-1] = dt.strptime(lst[-1], "%d-%m-%Y")
        else:
            messagebox.showerror("Ошибка", "Неверный формат даты")
            return

        note = create_note(lst[0], lst[1], lst[2], status, date_now, lst[-1])

        if validate_note(notes, note):
            # self._notes.append(note)
            notes.append(note)
            messagebox.showinfo("Выполнено", "Заметка успешно добавлена")
        else:
            messagebox.showerror("Ошибка", "Заметка стаким пользователем уже существует!")
            return


    def get_status(self):
        """Получение статуса"""
        return self.select_status.get()

    def focus_next_widget(self, event):
        """Переход к следующему виджету"""
        current_widget = event.widget
        index = self.entries.index(current_widget)  # Определяем текущий индекс
        if index < len(self.entries) - 1:
            # Переход к следующему полю
            self.entries[index + 1].focus_set()
        else:
            # Если это последнее поле, передаем фокус на кнопку
            self.but.focus_set()



class DisplayNotesFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        self._message = "Окно для отображения заметок"
        master.message_label.set(self._message)

        self.create_tree(notes)



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
        s = self.select()

        n = search_notes(notes, keyword=keyword, status=s)
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