import tkinter as tk
import customtkinter as ctk
from window import MainWindow

class MainApp:
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')
    def __init__(self):
        self.master = ctk.CTk()
        self.master.title('Login')

        self.width = 500
        self.height = 400
        self.sys_width = int((self.master.winfo_screenwidth() / 2) - self.width / 2)
        self.sys_height = int((self.master.winfo_screenheight() / 2) - self.height / 2)
        self.master.geometry(f'{self.width}x{self.height}+{self.sys_width}+{self.sys_height}')
        self.master.resizable(width=False, height=False)

        MainWindow(self.master)


if __name__ == '__main__':
    App = MainApp()