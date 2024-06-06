from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Frame

from pygame import mixer

from Models.Task import Task
from Views.taskDetail import TaskDetailView

class LoggedView(Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Images
        self.loupe_img = PhotoImage(file='assets\\loupe.png')
        
        # Study sound
        self.mixer = mixer
        self.mixer.init()
        self.mixer.music.load('assets/focus.mp3')
        self.mixer.music.set_volume(1)
        self.mixer.music.play(loops=-1)

        # Ajusting window size
        master.geometry('400x600')
        self['padding'] = "12 12 12 12"

        # Variables
        self.new_task_description = StringVar()
        self.search_task_description = StringVar()

        # Tratamento das tasks
        self.tasks = []

        # Top text  
        self.page_title = ttk.Label(self, text=f'Bem vindo, {self.master.user["userName"]}')
        self.page_title.configure(font=('monospace', 20))
        self.page_title.pack(side=TOP, pady=10)

        self.search_task_frame = ttk.Frame(self)
        self.search_task_frame.pack(fill='both', pady=10)

        self.search_task_entry = ttk.Entry(self.search_task_frame, textvariable=self.search_task_description)
        self.search_task_entry.pack(side=LEFT)
        self.search_task_entry.configure(width=25)

        self.search_task_button = ttk.Button(self.search_task_frame, command=self.search_task_by_desc, image=self.loupe_img, bootstyle=LIGHT)
        self.search_task_button.pack(side=LEFT, padx=5)

        self.tasks_list = Listbox(self, height=10)
        self.tasks_list.pack(fill='both')

        self.get_user_tasks()

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(fill='both')

        self.new_task_entry = ttk.Entry(self.form_frame, textvariable=self.new_task_description)
        self.new_task_entry.pack(side=LEFT, pady=10)
        self.new_task_entry.configure(width=25)

        self.add_task_button = ttk.Button(self.form_frame, command=self.add_new_task, text='Adicionar', bootstyle=SUCCESS)
        self.add_task_button.pack(side=LEFT, padx=20, pady=10)

        self.exit_button = ttk.Button(self, text='Sair', command=self.logout, bootstyle=DANGER)
        self.exit_button.pack(pady=20)

        self.tasks_list.bind("<Double-Button-1>", self.show_task_detail)

    def logout(self):
        self.mixer.quit()
        self.form_frame.pack_forget()
        self.master.login_view()

    def add_new_task(self):
        new_task = self.new_task_description.get()
        if not self.check_if_exists(new_task):
            Task.add_task(new_task, self.master.user['id'])
            self.new_task_description.set('')
            self.update_tasks()
        else:  
            messagebox.showerror('Tarefa já existente na lista!')

    def check_if_exists(self, taskDesc):
        exists = False
        for task in self.tasks:
            if task['taskDesc'] == taskDesc:
                exists = True
        return exists

    def update_tasks(self):
        self.get_user_tasks()

    def get_user_tasks(self):
        self.tasks = Task.get_user_tasks(self.master.user['id'])
    
        self.tasks_list.delete(0, END)

        for task in self.tasks:
            self.tasks_list.insert(END, task['taskDesc'])

        self.add_bg_color()

    def add_bg_color(self):
        for i in range(len(self.tasks)):
            if(self.tasks[i]['taskStatus'] == 'Done'):
                self.tasks_list.itemconfigure(i, background='#80ed99')
            else:
                self.tasks_list.itemconfigure(i, background='#f0f0ff')

    def show_task_detail(self, *args):
        task_selected = self.tasks_list.curselection()
        taskId = self.get_task_id(self.tasks_list.get(task_selected[0]))
        TaskDetailView(self, task=self.tasks_list.get(task_selected[0]), taskId=taskId)

    def get_task_id(self, taskDesc):
        for task in self.tasks:
            if task['taskDesc'] == taskDesc:
                return task['id']
            
    def search_task_by_desc(self):
        task_desc = self.search_task_description.get()
        task_list_desc = Task.get_task_by_description(task_desc, self.master.user['id'])

        self.tasks_list.delete(0, END)

        for task in task_list_desc:
            self.tasks_list.insert(END, task['taskDesc'])

        self.add_bg_color()