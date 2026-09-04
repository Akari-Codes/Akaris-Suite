import subprocess
import sys
import os
from pathlib import Path
import joblib
import yaml
class settings:
    def __init__():
        Cachy()
    def get_cache_path():
        cache_path_data = str(os.getcwd() + "/bin/sub/cache/")
        return cache_path_data
    def get_session_path():
        session_path_data = str(os.getcwd() + "/bin/sub/session-cache/")
        return session_path_data
class Cachy:
    def __init__(self):
        self.cache_path = Path(settings.get_cache_path())
        self.session_path = Path(settings.get_session_path())
        if not self.cache_path.exists():
            self.cache_path.mkdir(parents=True, exist_ok=True)
        if not self.session_path.exists():
            self.session_path.mkdir(parents=True, exist_ok=True)
        self.cache_container = []
        print("[Alert] Cacher Rutime Initialized!")
        return

    def session_save(self, name="session_default"):
        session_path = Path(str(self.session_path) + name + ".session")
        session_path.touch()
        joblib.dump(self.cache_container, session_path)
        return

    def session_load(self, name="session_default"):
        session_path = Path(str(self.session_path)+ name + ".session")
        session_path.touch()
        self.cache_container = joblib.load(session_path)
        return
    
    def session_clear(self, name="session_default"):
        session_path = Path(str(self.session_path)+ name + ".session")
        session_path.touch()
        os.remove(session_path)
        return
    
    def session_clear_all(self):
        listed_dir = os.listdir(Path(str(self.session_path)))
        for x in listed_dir:
            if x[-8:] == ".session":
                session_path = Path(str(self.session_path)+ x)
                session_path.touch()
                os.remove(session_path)
        return
    
    def deposit(self, data, id, multi=False):
        count = -1
        if multi == True:
            while count != len(id)-1:
                count = count + 1
                self.cache_container.append({"id":id[count],"data":data[count]})
                print("[Log] Cached item - " + id[count])
        else:
            self.cache_container.append({"id":id, "data":data})
            print("[Log] Cached item - " + id)
        return
    
    def withdraw(self, id, mode=0):
        count = -1
        for x in self.cache_container:
            count = count + 1
            if x["id"] == id:
                data = x["data"]
                if mode ==1:
                    self.cache_container.pop(count)
                    print("[Log] Passed item - " + id + " and removed from cache")
                else:
                    print("[Log] Passed item - " + id)
                break
        return data
    
    def destroy(self, id):
        count = -1
        for x in self.cache_container:
            count = count + 1
            if x["id"] == id:
                data = x["data"]
                self.cache_container.pop(count)
                print("[Log] Destroyed Cached item - " + id)
                break
        return
    
    def clear(self):
        print("[Alert] Clearing All Cached Items!")
        self.cache_container = []
        return
    
    def save(self, data, id):
        self.cache_container.append({"id":id, "data":data})
        print("[Log] Cached item - " + id)
        print("[Log] Making Local Save of Cached item...")
        cache_path = Path(str(self.cache_path))
        if not cache_path.exists():
            cache_path.mkdir()
        cache_file_path = Path(str(self.cache_path) + id + ".tmp")
        print(cache_path)
        cache_file_path.touch()
        for x in self.cache_container:
            if x["id"] == id:
                data = x["data"]
                break
        if data is list:
            joblib.dump(data, cache_file_path)
        else:
            with open(cache_file_path, 'w') as f:
                f.write(str(data))
        print("[Log] Local Save Made!")
        return
    
    def load(self, id):
        cache_path = Path(str(self.cache_path))
        cache_file_path = Path(str(self.cache_path) + id + ".tmp")
        try:
            with open(cache_file_path, 'r') as f:
                data = f.read()
        except:
            data = joblib.load(cache_file_path)
        for x in self.cache_container:
            if x["id"] == id:
                x["data"] = data
                break
        return data

    def save_item(self, id):
        cache_path = Path(str(self.cache_path))
        cache_path.mkdir()
        cache_file_path = Path(str(self.cache_path) + id + ".tmp")
        cache_file_path.touch()
        for x in self.cache_container:
            if x["id"] == id:
                data = x["data"]
                break
        if data is list:
            joblib.dump(data, cache_file_path)
        else:
            with open(cache_file_path, 'w') as f:
                f.write(str(data))
        return

    def destroy_item(self, id):
        cache_path = Path(str(self.cache_path))
        cache_file_path = Path(str(self.cache_path) + id + ".tmp")
        os.remove(cache_file_path)
        count = -1
        for x in self.cache_container:
            count = count + 1
            if x["id"] == id:
                data = x["data"]
                self.cache_container.pop(count)
                print("[Log] Destroyed Cached item - " + id)
                break
        return

    def unsave(self, id):
        cache_path = Path(str(self.cache_path))
        cache_file_path = Path(str(self.cache_path) + id + ".tmp")
        os.remove(cache_file_path)
    
    def clear_all(self):
        self.clear()
        files = os.listdir(Path(str(self.cache_path)))
        for x in files:
            os.remove(Path(str(self.cache_path) + x))
        return

    def edit(self, data, id, multi=False):
        if multi == True:
            count = -1
            while count != len(id)-1:
                for x in self.cache_container:
                    if x["id"] == id[count]:
                        x["data"] == data[count]
            return
        else:
            for x in self.cache_container:
                if x["id"] == id:
                    x["data"] == data
            return
settings.__init__()