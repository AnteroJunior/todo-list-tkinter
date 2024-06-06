from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Frame

from Models.Database import Database
from Utils.validators import Validators
from Utils.hash_password import HashPassword
from Models.User import User

class RegisterView(Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Variables  
        self.name = StringVar()
        self.email = StringVar()
        self.password = StringVar()

        # Top text
        self.page_title = ttk.Label(self, text='Register')
        self.page_title.configure(font=('monospace', 20))
        self.page_title.pack(side=TOP)
        
        # Labels
        self.name_label = ttk.Label(self, text='Nome').pack()
        self.name_entry = ttk.Entry(self, textvariable=self.name, width=30)
        self.name_entry.pack()

        self.email_label = ttk.Label(self, text='Email').pack()
        self.email_entry = ttk.Entry(self, textvariable=self.email, width=30)
        self.email_entry.pack()
        
        self.password_label = ttk.Label(self, text='Password').pack()
        self.password_entry = ttk.Entry(self, textvariable=self.password, width=30, show='*')
        self.password_entry.pack()

        # Buttons
        self.login_button = ttk.Button(self, text='Cadastrar', command=self.register, bootstyle=SUCCESS, width=20)
        self.login_button.pack(pady=10)
    
        self.register_button = ttk.Button(self, text='Cancelar', command=master.login_view, bootstyle=DANGER, width=20)
        self.register_button.pack(pady=5)

    def register(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()

        if(Database().check_user(email=email)):
            messagebox.showwarning(message='Email já está em uso!')
        else:
            if Validators.verify_email(email) and Validators.verify_password(password) and Validators.verify_name(name):
                new_user = User(name=name, email=email, password=(HashPassword.hash_password(password=password)))
                new_user.add_user()
                messagebox.showinfo(message='Cadastrado com sucesso!')
                self.name.set('')
                self.email.set('')
                self.password.set('')
            else:
                messagebox.showerror(message='Verifique as informações passadas.')