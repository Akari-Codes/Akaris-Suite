from tkinter import filedialog as fd
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pathlib import Path
import fc
def get(title="Open file", multi=False, fileTypes=[("All Files","*.*")]):
    if multi == False:
        data = str(fd.askopenfilename(title=title,initialdir='/',filetypes=fileTypes))
    else:
        data = list(fd.askopenfilenames(title=title,initialdir='/',filetypes=fileTypes))
    return data

def open(title="Open file", multi=False, fileTypes=[("All Files","*.*")]):
    if multi == False:
        file = str(fd.askopenfilename(title=title,initialdir='/',filetypes=fileTypes))
        data = fc.open(path=file)
    else:
        file = list(fd.askopenfilenames(title=title,initialdir='/',filetypes=fileTypes))
        data = fc.open(path=file, multi=True)
    return data

def dump(data, title="Save file", multi=False, fileTypes=[("All Files","*.*")]):
    if multi == False:
        file = str(fd.asksaveasfilename(title=title,initialdir='/',filetypes=fileTypes))
        fc.dump(path=file, data=data)
    else:
        file = list(fd.asksaveasfilenames(title=title,initialdir='/',filetypes=fileTypes))
        fc.dump(path=file, data=data, multi=True)
    return

def load(title="Open file", multi=False, fileTypes=[("All Files","*.*")]):
    if multi == False:
        file = str(fd.askopenfilename(title=title,initialdir='/',filetypes=fileTypes))
        data = fc.load(path=file)
    else:
        file = list(fd.askopenfilenames(title=title,initialdir='/',filetypes=fileTypes))
        data = fc.load(path=file, multi=True)
    return data

def save(data, title="Save file", fileTypes=[("All Files","*.*")]):
    file = str(fd.asksaveasfilename(title=title,initialdir='/',filetypes=fileTypes))
    fc.save(path=file, data=data)
    return

def directory(title="Open Folder", fileTypes=[("All Files","*.*")]):
    data = str(fd.askdirectory(title=title,initialdir='/',filetypes=fileTypes))
    return data

def destroy(title="Open file to delete", multi=False, fileTypes=[("All Files","*.*")]):
    if multi == False:
        file = str(fd.askopenfilename(title=title,initialdir='/',filetypes=fileTypes))
        fc.destroy(path=file)
    else:
        file = list(fd.askopenfilenames(title=title,initialdir='/',filetypes=fileTypes))
        fc.destroy(path=file, multi=True)
        return

def erase(title="Open file to delete", multi=False, fileTypes=[("All Files","*.*")]):
    if multi == False:
        file = str(fd.askopenfilename(title=title,initialdir='/',filetypes=fileTypes))
        fc.erase(path=file)
    else:
        file = list(fd.askopenfilenames(title=title,initialdir='/',filetypes=fileTypes))
        fc.erase(path=file, multi=True)
    return
