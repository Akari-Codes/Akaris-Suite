from tkinter import filedialog as fd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pathlib import Path
try:
    import fc
except:
    print("[Error] File Core (fc) Module not found File Browser (fb) can not run without File core (fc) please install File core (fc)")
    quit()

def open(multi=False):
    if multi == False:
        data = str(fd.askopenfilename(title='Open file',initialdir='/'))
    else:
        data = list(fd.askopenfilenames(title='Open file',initialdir='/'))
    return data

def read(multi=False):
    if multi == False:
        file = str(fd.askopenfilename(title='Open file',initialdir='/'))
        data = fc.open(path=file)
    else:
        file = list(fd.askopenfilenames(title='Open file',initialdir='/'))
        data = fc.open(path=file, multi=True)
    return data

def dump(data, multi=False):
    if multi == False:
        file = str(fd.asksaveasfilename(title='Save file',initialdir='/'))
        fc.dump(path=file, data=data)
    else:
        file = list(fd.asksaveasfilenames(title='Save file',initialdir='/'))
        fc.dump(path=file, data=data, multi=True)
    return

def load(multi=False):
    if multi == False:
        file = str(fd.askopenfilename(title='Open file',initialdir='/'))
        data = fc.load(path=file)
    else:
        file = list(fd.askopenfilenames(title='Open file',initialdir='/'))
        data = fc.load(path=file, multi=True)
        
def save(data, multi=False):
    if multi == False:
        file = str(fd.asksaveasfilename(title='Save file',initialdir='/'))
        fc.save(path=file, data=data)
    else:
        file = list(fd.asksaveasfilenames(title='Save file',initialdir='/'))
        fc.save(path=file, data=data, multi=True)
    return

def directory():
    data = str(fd.askdirectory(title='Select Directory',initialdir='/'))
    return data

def destroy(multi=False):
    if multi == False:
        file = str(fd.askopenfilename(title='Open file to delete',initialdir='/'))
        fc.destroy(path=file)
    else:
        file = list(fd.askopenfilenames(title='Open file to delete',initialdir='/')) 
        fc.destroy(path=file, multi=True)
        return
    
def erase(multi=False):
    if multi == False:
        file = str(fd.askopenfilename(title='Open file to delete',initialdir='/'))
        fc.erase(path=file)
    else:
        file = list(fd.askopenfilenames(title='Open file to delete',initialdir='/'))
        fc.erase(path=file, multi=True)
    return
