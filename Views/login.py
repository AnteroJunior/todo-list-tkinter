from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Frame

from Utils.hash_password import HashPassword
from Utils.validators import Validators
from Models.Database import Database

class LoginView(Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        # Variables  
        self.email = StringVar()
        self.password = StringVar()

        # Top text
        self.page_title = ttk.Label(self, text='To Do List')
        self.page_title.configure(font=('monospace', 20))
        self.page_title.pack(side=TOP)
        
        # Labels
        self.name_label = ttk.Label(self, text='Email').pack()
        self.name_entry = ttk.Entry(self, textvariable=self.email, width=30).pack()

        self.password_label = ttk.Label(self, text='Password').pack()
        self.password_entry = ttk.Entry(self, textvariable=self.password, width=30, show='*')
        self.password_entry.pack()

        # Buttons
        self.login_button = ttk.Button(self, text='Entrar', command=self.verify_identity, bootstyle=SUCCESS, width=20)
        self.login_button.pack(pady=10)
    
        self.register_button = ttk.Button(self, text='Registrar', command=master.register_view, bootstyle=(INFO, OUTLINE), width=20)
        self.register_button.pack(pady=5)

        # Text
        self.author = ttk.Label(self, text='Developed by Antero Junior')
        self.author.pack(side=BOTTOM)

        self.password_entry.bind('<Return>', self.verify_identity)

    def verify_identity(self, *args):
        if(Validators.verify_email(self.email.get()) and Validators.verify_password(self.password.get())):
            user_credentials = Database().check_user(self.email.get())
            
            dict_user_credentials = {
                'id': user_credentials[0],
                'userName': user_credentials[1],
                'userEmail': user_credentials[2],
                'userPassword': user_credentials[3]
            }

            if(user_credentials and HashPassword.check_password(dict_user_credentials['userPassword'], self.password.get())):
                self.master.user = dict_user_credentials
                self.master.user_view()
            else:
                messagebox.showerror(message='Credenciais incorretas. Verifique e tente novamente.')                
        else:
            messagebox.showerror(message='Valores não permitidos!')