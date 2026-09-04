import os
import sys
import pickle
import subprocess
import time
from pathlib import Path
import shutil
from halo import Halo
def cls():
    os.system('cls')

def load_interface(name, index):
    with open(Path(os.getcwd() + "\\bin\\ui\\command_line\\" + name + "\\" + index + ".ui"), 'r') as program:
        data = pickle.loads(bytes(str(pickle.dumps(program.read()), encoding="latin1"), "latin1"))
    print(data)
    return

def make_interface(path, name, index):
    source_loco = Path(path)
    dest_loco = Path(os.getcwd() + "\\bin\\ui\\command_line\\" + name + "\\" + index + ".ui")
    Path(os.getcwd() + "\\" + name + "\\").mkdir()
    shutil.copy(source_loco, dest_loco)
    return 1
    
def edit_interface(name, index):
    dest_loco = Path(os.getcwd() + "\\bin\\ui\\command_line\\" + name + "\\" + index + ".ui")
    a = """start notepad """ + dest_loco
    os.system(a)
    return 

def load_reactive_interface(name,index,data_archive):
    data = load_interface(name, index)
    array = data.split("^*^")
    z = -1
    y = 0
    for x in array:
        z = z + 1
        if x == "^*^":
            array[z] = data_archive[y]
            y = y + 1
    data = " ".join(array)
    print(data)
    return
    
    
def reload_interface(name,index,data_archive):
    cls()
    data = load_reactive_interface(name,index,data_archive)
    print(data)
    return

class loader:
    def start(self, data):
        animation = Halo(text=data, spinner='dots')
        animation.start()
    def stop(self):
        self.animation.stop()
    def succeed(self, data):
        self.animation.succeed(data)
    def fail(self,data):
        self.animation.fail(data)
    def warn(self, data):
        self.animation.warn(data)

def wait(time_period):
    time.sleep(time_period)
    return

def pause():
    input()
    return