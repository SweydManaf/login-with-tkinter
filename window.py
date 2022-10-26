import customtkinter as ctk
from tkinter import messagebox

class MainWindow:
    def __init__(self, master):
        self.root = master

        self.labelLogin = ctk.CTkLabel(self.root,
                                       text='Login',
                                       text_color='white',
                                       text_font='Open 16 bold',
                                       width=10, height=10)

        self.nameEntry = ctk.CTkEntry(self.root,
                                      placeholder_text='Username',
                                      width=150, height=5)
        self.passwordEntry = ctk.CTkEntry(self.root,
                                          placeholder_text='Password', show='*',
                                      width=150, height=5)

        self.loginButton = ctk.CTkButton(self.root,
                                         text='LOGIN')
        self.loginButton.configure(command=self.processLogin)

        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.labelLogin.grid(row=0, column=0, pady=(90, 20), )
        self.nameEntry.grid(row=1, column=0, padx=190, pady=(0, 10))
        self.passwordEntry.grid(row=2, column=0, pady=(10, 20))
        self.loginButton.grid(row=4, column=0, pady=(0, 10))

    def processLogin(self):
        self.username = self.nameEntry.entry.get()
        self.password = self.passwordEntry.entry.get()

        if self.username == '' or self.username == 'Username':
            messagebox.showwarning(message='Informe o nome de usuário!')
        elif self.password == '' or self.password == 'Password':
            messagebox.showwarning(message='Informe a senha do Usuário!')
        else:
            if self.username == 'sweyd' and self.password == '123':
                messagebox.showinfo(message='Sessão iniciada.')
                self.nameEntry.delete(0, 'end')
                self.passwordEntry.delete(0, 'end')
                self.root.focus()
