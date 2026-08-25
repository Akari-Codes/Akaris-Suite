import py7zr
from pathlib import Path
import halo
import time
import os

def cls():
    os.system('cls')

def start():
    cls()
    print("Enter Path to folder with application files:")
    print()
    def l1():
        try:
            path = Path(input(" > "))
            return path
        except:
            print("Invalid path. Please try again.")
            time.sleep(1)
            start()
    path = l1()
    cls()
    s1 = halo.Halo(text='Compressing files...', spinner='bounce')
    s1.start()
    py7zr.pack_7zarchive(path, Path(os.getcwd() + "/program.7z"))
    s1.succeed("Files compressed successfully.")
    time.sleep(3)
    quit()
    
