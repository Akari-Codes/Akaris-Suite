import os
import time
from pathlib import Path
import joblib
import py7zr
import webview
tos = """"""
config = {"name":"","body":"","tos":tos,"path":"","version":"","author":"","finish":"","fail":""}
def startUp():
    leftPanel = """"""
    icon = """"""
    Path(os.getcwd() + "/leftpanel.png").touch()
    Path(os.getcwd() + "/icon.png").touch()
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

    elif name == "install":
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
        window.get_element('#title').text = "Welcome to " + config["name"] + "Installer"
        window.get_element('#desc').text = config["body"]
        window.get_element('#author').text = config["author"]
        window.get_element('#version').text = config["version"]

    def acceptTOS(self, yn):
        if yn == "yes":
            self.setPath()
        else:
            self.failInstall()
            
    def startInstall(self, path):
        install(Path(path), programData, window)

    def setPath(self):
        window.load_html(ui("changePath"))
        window.get_element('#path').text = config["path"]

    def finishInstall(self):
        window.load_html(ui("finishInstall"))
        window.get_element('#desc').text = config["finish"]
        window.get_element('#title').text = config["name"]
        window.get_element('#version').text = config["version"]
        window.get_element('#author').text = config["author"]

    def TOS(self):
        window.load_html(ui("TOS"))
        window.get_element('#tos').text = config["tos"]
        window.get_element('#title').text = config["name"]

    def failInstall(self):
        window.load_html(ui("failInstall"))
        window.get_element('#desc').text = config["fail"]
        window.get_element('#title').text = config["name"]
        window.get_element('#version').text = config["version"]
        window.get_element('#author').text = config["author"]

    def startUp(self):
        window.load_html(ui("startUp"))
        window.get_element('#title').text = "Welcome to " + config["name"] + "Installer"
        window.get_element('#desc').text = config["body"]
        window.get_element('#author').text = config["author"]
        window.get_element('#version').text = config["version"]

if __name__ == "__main__":
    Api = api()
    window = webview.create_window("Installer", html=ui("startUp"), js_api=Api, width=600, height=400)
    webview.start()