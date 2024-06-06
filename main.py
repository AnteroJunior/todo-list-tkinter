from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from Views import *
from Models.Database import Database

class App(ttk.Window):

    def __init__(self) -> None:
        super().__init__()
        self.title("To Do List")
        self.geometry('380x400')

        self.resizable(FALSE, FALSE)
        self.main_frame = LoginView(master=self)
        self.main_frame.pack(fill='both')

        self.user = None

    def login_view(self):
        self.main_frame.pack_forget()
        self.user = None
        self.main_frame = LoginView(master=self)
        self.main_frame.pack(fill='both')

    def register_view(self):
        self.main_frame.pack_forget()
        self.main_frame = RegisterView(master=self)
        self.main_frame.pack(fill='both')
   
    def user_view(self):
        self.main_frame.pack_forget()
        self.main_frame = LoggedView(master=self)
        self.main_frame.pack(fill='both')

if __name__ == '__main__':
    # Creating database
    db = Database()
    db.create_tables()
    
    App().mainloop()