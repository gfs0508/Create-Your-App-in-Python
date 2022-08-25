from ast import Return
from asyncio.windows_events import NULL
import new
import open_
import csv
from tkinter import *
from extensions import superExtensions


def load_rt(win_rt):
    btn = Button(win_rt,text="Extensions").place(x=155, y=320)
    superExtensions.superEx(win_rt)

def load(root):
    print("Loading Extensions ... ")
    print("=======================")
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            pass

    print(f'Loader Version: {row["version_loader"]}')
    print(f'Framework Version: {row["version_framework"]}')
    load_rt(root)
    

    