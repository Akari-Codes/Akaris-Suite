from cachy import Cachy
import os
import fc
import krypt
import webview
from webview import *
from pathlib import Path
import time
cache = Cachy()

def get_passd():
    passd = cache.withdraw(id="password")
    return passd

def set_passd(passd):
    passd = krypt.new_pass(password=passd)
    cache.deposit(id="password", data=passd)
    if fc.exists(path=os.getcwd() + "/bin/local/pass_cache.dat"):
        fc.dump(path=os.getcwd() + "/bin/local/pass_cache.dat", data=passd)
    else:
        fc.mkdir(path=os.getcwd() + "/bin/local/")
        fc.touch(path=os.getcwd() + "/bin/local/pass_cache.dat")
        fc.dump(path=os.getcwd() + "/bin/local/pass_cache.dat", data=passd)
    return

def load_pass():
    passd = fc.load(path=os.getcwd() + "/bin/local/pass_cache.dat")
    cache.deposit(id="password", data=passd)
    return

class Api:
    def interface(self,ui):
        window.load_html(fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/" + ui + ".ui")))
        return

    def change_passd(self):
        passd = window.dom.get_element('#passd')
        set_passd(passd)

    def home_and_change_passd(self):
        passd = window.dom.get_element('#passd').value
        set_passd(passd)
        self.interface(ui="home")

    def encryption(self):
        file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=True, file_types=('All files (*.*)')))
        passd = get_passd()
        for x in file:
            data = krypt.full_enc(password=passd, data=fc.open(path=x))
            fc.write(path=x, data=data)

    def decrytpion(self):
        file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=True, file_types=('All files (*.*)')))
        passd = get_passd()
        for x in file:
            data = krypt.full_dec(password=passd, data=fc.open(path=x))
            fc.write(path=x, data=data)

    def editor(self):
        cache.deposit(id="edtior_toggle_states", data=[False])
        cache.deposit(id="editor_saved", data=False)
        cache.deposit(id="editor_current_open", data="!NONE!")
        self.interface(ui="editor")
        window.dom.get_element('#status').text = "*"

    def editor_quit(self):
        if cache.withdraw(id="editor_saved") == False:
            if not window.dom.get_element('#text_box').value == "":
                if window.create_confirmation_dialog("Editor", "File Not Saved do you Wish to Exit") == True:
                    self.interface(ui="encryption")

    def editor_open(self):
        passd = get_passd()
        file = str(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=False, file_types=['Encrypted Secrets Text Files (*.secret)']))
        file = file.replace("('","")
        file = file.replace("',)","")
        cache.deposit(id="editor_current_open", data=file)
        cache.deposit(id="editor_saved", data=True)
        data = fc.open(file)
        data = krypt.full_dec(password=passd, data=data)
        window.dom.get_element('#text_box').text = data
        window.dom.get_element('#status').text = file + " - Saved"

    def editor_save(self):
        passd = get_passd()
        data = window.dom.get_element('#text_box').value
        path = cache.withdraw(id="editor_current_open")
        if not path == "!NONE!":
            cache.deposit(id="editor_saved", data=True)
            data = krypt.full_enc(password=passd, data=data)
            fc.write(data=data, path=path)
            window.dom.get_element('#status').text = path + " - Saved"
        else:
            self.editor_save_as()

    def editor_save_as(self):
        passd = get_passd()
        data = window.dom.get_element('#text_box').value
        path = str(window.create_file_dialog(webview.FileDialog.SAVE, allow_multiple=False, file_types=['Encrypted Secrets Text Files (*.secret)']))
        path = path.replace("('","")
        path = path.replace("',)","")
        fc.touch(path)
        data = krypt.full_enc(password=passd, data=data)
        fc.write(path=path, data=data)
        cache.deposit(id="editor_current_open", data=path)
        cache.deposit(id="editor_saved", data=True)
        window.dom.get_element('#status').text = path + " - Saved"

    def editor_new(self):
        cache.deposit(id="editor_current_open", data="!NONE!")
        cache.deposit(id="editor_saved", data=False)
        window.dom.get_element('#status').text = "*"
    
    def editor_new_as(self):
        passd = get_passd()
        path = str(window.create_file_dialog(webview.FileDialog.SAVE, allow_multiple=False, file_types=['Encrypted Secrets Text Files (*.secret)']))
        path = path.replace("('","")
        path = path.replace("',)","")
        fc.touch(path)
        window.dom.get_element('#text_box').text = "Enter Text Here..."
        data = data = window.dom.get_element('#text_box').value
        data = krypt.full_enc(password=passd, data=data)
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

    def edtior_file_ribbon_toggle(self):
        toggles = cache.withdraw(id="edtior_toggle_states")
        if toggles[0] == False:
            toggle = True
            toggles[0] = toggle
            cache.deposit(id="edtior_toggle_states", data=toggles)
            window.dom.get_element('#ribbon').style['display'] = "block"
            window.dom.get_element('#text_box').style['height'] = "81%"
        else:
            toggle = False
            toggles[0] = toggle
            cache.deposit(id="edtior_toggle_states", data=toggles)
            window.dom.get_element('#ribbon').style['display'] = "none"
            window.dom.get_element('#text_box').style['height'] = "90%"

def on_closed():
    quit()

if __name__ == "__main__":
    api = Api()
    if fc.exists(path=os.getcwd() + "/bin/local/pass_cache.dat"):
        load_pass()
        html_data = fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/home.ui"))
    else:
        html_data = fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/set_pass.ui"))
    window = webview.create_window("Akari's Suite", html=html_data, js_api=api, confirm_close=True)
    window.events.closed += on_closed
    webview.start()
