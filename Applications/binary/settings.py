import Applications.binary.fc as fc
import pickle
import os
from pathlib import Path
from Applications.MangaReader.cachy_sub import Cachy
cache = Cachy()
def init(name, path=False, settings_data=False):
    if path == False:
        path = os.getcwd() + "/bin/settings/"
    if not Path(path + name + ".conf").exists() == True:
        fc.mkdir(path)
        fc.touch(path=path + name + ".conf")
    if not settings_data == False:
        fc.dump(data=settings_data, path=path + name + ".conf")
    cache.deposit(data=path + name + ".conf", id="settings_config_file")
    cache.deposit(data=fc.load(path=path + name + ".conf"), id="settings")
    return
    
def update_settings(settings):
    path = cache.withdraw(id="settings_config_file")
    cache.deposit(data=str(settings), id="settings")
    fc.dump(data=str(settings), path=path)
    return

def change_settings(id, data):
    path = cache.withdraw(id="settings_config_file")
    settings = pickle.loads(cache.withdraw(id="settings"))
    settings[id] = data
    cache.deposit(data=str(settings), id="settings")
    fc.dump(data=str(settings), path=path)
    return

def get_all_settings():
    return pickle.loads(cache.withdraw(id="settings"))
    
def get_setting(id):
    settings = pickle.loads(cache.withdraw(id="settings"))
    data = settings[id]
    return data