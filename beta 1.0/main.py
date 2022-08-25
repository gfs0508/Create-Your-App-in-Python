from hashlib import new
from tkinter import *
import csv
from styles import style1
from new import new_project
from open_ import open_project
import loader
from accont import login

root = Tk()
root.geometry("400x350")
root.resizable(False, False)

with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        pass

print(f'Version: {row["version"]}')
print(f'Selected Language: {row["lang_selected"]}')

if(f'{row["extensions_load"]}' == "yes"):
    loader.load(root)

file.close()

with open(f'{row["lang_selected"]}', mode='r') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        pass

title = Label(root, text=f'{row["title1"]}', **style1.title1).grid(row=0, column=0, sticky=W, pady=2)
accont_btn = Button(root, text="CONTA", command=login).place(x=5,y=320)
settings_btn = Button(root, text=f'{row["settings"]}', bd = '2',**style1.button2).place(x=60, y=320)


def new_project_load():
    window_root = root
    new_project(window_root)
def open_project_load():
    window_root = root
    open_project(window_root)

new_project_btn = Button(root, text=f'{row["new_project"]}', bd = '0.5',**style1.button1, command=new_project_load).grid(row=1, column=0, sticky=W, pady=2, padx=5)
open_project_btn = Button(root, text=f'{row["open_project"]}', bd = '0.5',**style1.button1, command=open_project_load).grid(row=2, column=0, sticky=W, pady=2, padx=5)
quit_btn = Button(root, text=f'{row["quit"]}', bd = '0.5',**style1.button1, command=root.destroy).grid(row=3, column=0, sticky=W, pady=2, padx=5)

root.title(f'{row["title1"]}')

root.mainloop()