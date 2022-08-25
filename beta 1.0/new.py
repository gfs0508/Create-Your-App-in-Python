from tkinter import *
import csv
from tkinter import messagebox
from styles import style1
from loader import *
from pathlib import Path
import os

def newProject(row, e1):
    try:
        project_name = e1.get()
        project = f'./projects/{project_name}'
        print(project_name)
        os.mkdir(project)
    except:
        messagebox.showinfo(title=f'{row["error"]}', message=f'{row["project_exists"]}')

    try:
        debugfolder = './projects/teste1/debug'
        os.mkdir(debugfolder)
    except:
        messagebox.showinfo(title=f'{row["error"]}', message=f'{row["error_create"]} debug')

    try:
        fileproject1 = Path('projects/teste1/data.csv')
        fileproject1.touch(exist_ok=True)
    except:
        messagebox.showinfo(title=f'{row["error"]}', message=f'{row["error_create"]} data.csv')

    try:
        fileproject2 = Path('projects/teste1/main.py')
        fileproject2.touch(exist_ok=True)
    except:
        messagebox.showinfo(title=f'{row["error"]}', message=f'{row["error_create"]} main.py')

        
def new_project(window_root):
    
    new_project = Tk()
    new_project.resizable(False, False)
    new_project.geometry("350x250")
    window_root.destroy()

    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            pass
    file.close()
    with open(f'{row["lang_selected"]}', mode='r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            pass


    title = Label(new_project, text = f"{row['new_project']}", **style1.title1).grid(row=0, column=0, sticky= W, pady = 2)

    l1 = Label(new_project, text = f"{row['insert_new_project']}").grid(row = 2, column = 0, sticky = W, pady = 2)
    l2 = Label(new_project, text = f"{row['autor']}").grid(row = 3, column = 0, sticky = W, pady = 2)
    l3 = Label(new_project, text = f"{row['version']}").grid(row = 4, column = 0, sticky = W, pady = 2)
    
    e1 = Entry(new_project).grid(row = 2, column = 1, pady = 2)
    e2 = Entry(new_project).grid(row = 3, column = 1, pady = 2)
    e3 = Entry(new_project).grid(row = 4, column = 1, pady = 2)

    
    btn1 = Button(new_project, text=f"{row['new_project']}", **style1.button1, command=newProject(row, e1)).place(x=100, y=200)
 

    new_project.title(f'{row["new_project"]}')
    new_project.mainloop()




    
    
    