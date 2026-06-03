from cachy_sub import Cachy as cache
import os
import fc
import fb
import krypt
import settings
import webview
from webview import *
from pathlib import Path
import tkinter
import time

def gui():
    class Api:
        def inteface(self,ui):
            window.load_html(fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/" + ui + ".ui")))
            return

        def enc(self):
            mode = str(window.dom.get_element("#app-mode").value())
            if mode == "enc":
                file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=True, file_types=('All files (*.*)')))
                user_info = cache.withdraw(id="user_info")
                for x in file:
                    data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=fc.open(path=x))
                    fc.write(path=x, data=data)
            elif mode == "dec":
                file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=True, file_types=('All files (*.*)')))
                for x in file:
                    data = krypt.full_dec(username=user_info["username"], password=user_info["password"], data=fc.open(path=x))
                    fc.write(path=x, data=data)
            elif mode == "editor":
                cache.deposit(id="editor_saved", data=False)
                cache.deposit(id="editor_current_open", data="!NONE!")
                self.interface(ui="editor")
                window.dom.get_element('#status').text = "*"

        def editor_quit(self):
            if cache.withdraw(id="editor_saved") == False:
                if not window.get_element('#text_box').value == "":
                    if window.create_confirmation_dialog("Editor", "File Not Saved do you Wish to Exit") == True:
                        self.interface(ui="encryption")
 
        def editor_open(self):
            user_info = cache.withdraw(id="user_info")
            file = str(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=False, file_types=('Encrypted Secrets Text Files (*.secret)')))
            cache.deposit(id="editor_current_open", data=file)
            cache.deposit(id="editor_saved", data=True)
            data = fc.open(file)
            data = krypt.full_dec(username=user_info["username"], password=user_info["password"], data=data)
            window.dom.get_element('#text_box').text = data
            window.dom.get_element('#status').text = file + " - Saved"

        def editor_save(self):
            user_info = cache.withdraw(id="user_info")
            data = window.dom.get_element('#text_box').value
            path = cache.withdraw(id="editor_current_open")
            if not path == "!NONE!":
                cache.deposit(id="editor_saved", data=True)
                data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
                fc.write(data=data, path=path)
                window.dom.get_element('#status').text = path + " - Saved"
            else:
                self.editor_save_as()

        def editor_save_as(self):
            user_info = cache.withdraw(id="user_info")
            data = window.dom.get_element('#text_box').value
            path = str(window.create_file_dialog(webview.FileDialog.SAVE, allow_multiple=False, file_types=('Encrypted Secrets Text Files (*.secret)')))
            fc.touch(path)
            data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
            fc.write(path=path, data=data)
            cache.deposit(id="editor_current_open", data=path)
            cache.deposit(id="editor_saved", data=True)
            window.dom.get_element('#status').text = path + " - Saved"

        def editor_new(self):
            cache.deposit(id="editor_current_open", data="!NONE!")
            cache.deposit(id="editor_saved", data=False)
            window.dom.get_element('#status').text = "*"
        
        def new_as(self):
            user_info = cache.withdraw(id="user_info")
            path = str(window.create_file_dialog(webview.FileDialog.SAVE, allow_multiple=False, file_types=('Encrypted Secrets Text Files (*.secret)')))
            fc.touch(path)
            window.dom.get_element('#text_box').text = "Enter Text Here..."
            data = data = window.dom.get_element('#text_box').value
            data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
            fc.write(path=path, data=data)
            cache.deposit(id="editor_current_open", data=path)
            cache.deposit(id="editor_saved", data=True)
            window.dom.get_element('#status').text = path + " - Saved"
            
        def editor_unsaved(self):
            time.sleep(3)
            cache.deposit(id="editor_saved", data=False)
            if cache.withdraw(id="editor_current_open") == "!NONE!":
                window.dom.get_element('#status').text = "* - Not Saved"
            else:
                path = cache.withdraw(id="editor_current_open")
                window.dom.get_element('#status').text = path + "* - Not Saved"
        
        def editor_clear(self):
            cache.deposit(id="editor_saved", data=False)
            cache.deposit(id="editor_current_open", data="!NONE!")
            window.dom.get_element('#text_box').text = ""
            window.dom.get_element('#status').text = "*"

    def on_closed():
        quit()

    if __name__ == "__main__":
        api = Api()
        window = webview.create_window("Akari's Suite", html=fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/home.ui")), js_api=api, confirm_close=True)
        window.events.closed += on_closed
        webview.start()
    return
def start(user_info):
    cache.deposit(id="user_info", data=user_info)
    gui()