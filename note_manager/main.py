import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Добро пожаловать в менеджер заметок")
        self.geometry("531x376+796+359")
        self.resizable(False, False)
        self.current_frame = None

        self.show_frame(StartFrame)

    def show_frame(self, frame_class):
        """Показать указанное окно"""
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(expand=True, fill="both")

class StartFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Кнопка "Создать файл"
        create_file_btn = tk.Button(self, text="Создать новую заметку", command=lambda: master.show_frame(CreateNoteFrame))
        create_file_btn.pack(pady=20)

        # Кнопка "Завершить программу"
        exit_btn = tk.Button(self, text="Завершить программу", command=self.exit_program)
        exit_btn.pack(pady=20)

    def exit_program(self):
        """Подтверждение выхода из программы"""
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.master.destroy()

class CreateNoteFrame(tk.Frame):
    pass

class DisplayNotesFrame(tk.Frame):
    pass

class UpdateNoteFrame(tk.Frame):
    pass