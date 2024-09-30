import tkinter as tk

class Window(tk.Tk):
    def __init__(self, title='My App', geometry='800x400'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

    def add_label(self, text='Hello, World!', font=('Arial', 12), padding=10):
        label = tk.Label(self, text=text, font=font)
        label.pack(padx=padding, pady=padding)
