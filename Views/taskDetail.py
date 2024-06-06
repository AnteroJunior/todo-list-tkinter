from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Frame

from Models.Task import Task

class TaskDetailView(Toplevel):

    def __init__(self, master, task, taskId, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        # Images
        self.save_img = PhotoImage(file='assets\\save.png')
        self.trash_img = PhotoImage(file='assets\\trash.png')
        self.inprogress_img = PhotoImage(file='assets\\loading.png')
        self.done_img = PhotoImage(file='assets\\finish.png')

        # Window config 
        self.geometry('380x300')
        self['padx'] = 20
        self['pady'] = 20

        # Variables
        self.task = task
        self.taskId = taskId

        # Form
        self.task_frame = Frame(self)
        self.task_frame.pack(fill='x', pady=(0, 0))

        self.task_description = StringVar()
        self.task_description.set(value=task)

        self.task_description_entry = ttk.Entry(self.task_frame, textvariable=self.task_description, width=30)
        self.task_description_entry.pack(side='left')

        self.save_task_update_button = ttk.Button(self.task_frame, command=self.update_task, image=self.save_img, bootstyle=(OUTLINE, LIGHT))
        self.save_task_update_button.pack(side='left', padx=10)
        
        # Action buttons
        self.action_frame = Frame(self)
        self.action_frame.pack(fill='x', pady=(10, 0))

        self.finish_button = ttk.Button(self.action_frame, command=self.mark_as_done, image=self.done_img, bootstyle=(OUTLINE, LIGHT))
        self.finish_button.pack(side=LEFT)

        self.inprogress_button = ttk.Button(self.action_frame, command=self.mark_as_inprogress, image=self.inprogress_img, bootstyle=(OUTLINE, LIGHT))
        self.inprogress_button.pack(side=LEFT, padx=10)

        self.delete_button = ttk.Button(self.action_frame, command=self.delete_task, image=self.trash_img, bootstyle=(OUTLINE, LIGHT))
        self.delete_button.pack(side=LEFT)

    # Methods
    def update_task(self):
        task_desc = self.task_description.get()
        if not self.master.check_if_exists(task_desc):
            Task.update_task(self.taskId, task_desc)
            messagebox.showinfo(message='Tarefa atualizada com sucesso!')
            self.master.update_tasks()
            self.destroy()
        else:
            messagebox.showerror(message='Tarefa já existe!')

    def mark_as_done(self):
        Task.mark_as_done(self.taskId)
        messagebox.showinfo(message='Tarefa concluída com sucesso!')
        self.master.update_tasks()
        self.destroy()

    def mark_as_inprogress(self):
        Task.mark_as_inprogress(self.taskId)
        messagebox.showinfo(message='Tarefa atualizada para: em andamento!')
        self.master.update_tasks()
        self.destroy()

    def delete_task(self):
        Task.delete_task(self.taskId)
        messagebox.showinfo(message='Tarefa removida com sucesso!') 
        self.master.update_tasks()
        self.destroy()