import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Добро пожаловать в менеджер заметок")
        self.geometry("531x376+796+359")
        self.resizable(False, False)
        self.current_frame = None
        self.previous_frame = None

        self.show_frame(StartFrame)

    def show_frame(self, frame_class):
        """Показать указанное окно"""
        if self.current_frame:
            self.previous_frame = self.current_frame.__class__
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(expand=True, fill="both")

    def go_back(self):
        """Вернуться к предыдущему окну"""
        if self.previous_frame:
            self.show_frame(self.previous_frame)
        
class BaseFrame(tk.Frame):
    def __init__(self, master: App):
        super().__init__(master)

        back_btn = ttk.Button(self, text="Вернуться в предыдущее меню", command=master.go_back, width=30)
        back_btn.pack(side="bottom", pady=40)

class StartFrame(tk.Frame):
    def __init__(self, master: App):
        super().__init__(master)

        # Кнопка "Создать файл"
        create_note_btn = ttk.Button(self, text="Создать новую заметку", width=30,
                                    command=lambda: master.show_frame(CreateNoteFrame))
        create_note_btn.pack(pady=6)


        display_notes_btn = ttk.Button(self, text="Показать все заметки", width=30,
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



        # Кнопка "Завершить программу"
        exit_btn = ttk.Button(self, text="Завершить программу", command=self.exit_program, width=30)
        exit_btn.pack(anchor="s", expand=True, pady=40)

    def exit_program(self):
        """Подтверждение выхода из программы"""
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.master.destroy()

class CreateNoteFrame(BaseFrame):
    pass


class DisplayNotesFrame(BaseFrame):
    pass


class UpdateNoteFrame(BaseFrame):
    pass

class DeleteNoteFrame(BaseFrame):
    pass


class SearchNoteFrame(BaseFrame):
    pass

if __name__ == '__main__':
    app = App()
    app.mainloop()