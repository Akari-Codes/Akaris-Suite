import os
import time
from pathlib import Path
import joblib
import py7zr
import webview

def startUp():
    config = """"""
    leftPanel = """"""
    icon = """"""
    Path(os.getcwd() + "/config.conf").touch()
    Path(os.getcwd() + "/leftpanel.png").touch()
    Path(os.getcwd() + "/icon.png").touch()
    with open(Path(os.getcwd() + "/config.conf"), "w") as f:
        f.write(config)
    with open(Path(os.getcwd() + "/leftpanel.png"), "w") as f:
        f.write(leftPanel)  
    with open(Path(os.getcwd() + "/icon.png"), "w") as f:
        f.write(icon)
    
def ui(name):
    if name == "startUp":
        return """"""
    
    elif name == "TOS":
        return """"""
    
    elif name == "changePath":
        return """"""
    
    elif name == "finishInstall":
        return """"""
    
    elif name == "failInstall":
        return """"""

programData = """"""

def install(dest, programData, window):
    Path(os.getcwd() + "/program.7z").touch()
    with open(Path(os.getcwd() + "/program.7z"), "w") as f:
        f.write(programData)
    py7zr.unpack_7zarchive(Path(os.getcwd() + "/program.7z"), dest)
    os.remove(Path(os.getcwd() + "/program.7z"))

class api:
    def __init__(self):
        

    def acceptTOS(self, yn):
        if yn == "yes":
            self.setPath()
        else:
            self.failInstall()
            
    def startInstall(self, path):
        install(Path(path), programData, window)

    def setPath(self):
        window.load_html(ui("changePath"))

    def finishInstall(self):
        window.load_html(ui("finishInstall"))

    def TOS(self):
        window.load_html(ui("TOS"))

    def failInstall(self):
        window.load_html(ui("failInstall"))

    def startUp(self):
        window.load_html(ui("startUp"))

if __name__ == "__main__":
    Api = api()
    window = webview.create_window("Installer", html=ui("startUp"), js_api=Api, width=600, height=400)
    webview.start()