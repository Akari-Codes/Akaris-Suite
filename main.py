from cachy_sub import Cachy as cache
import os
import fc
import fb
import krypt
import settings
import webview
import cli
from pathlib import Path
import tkinter
settings_template = {
    {"interface":"gui"}
}
settings.init(name="main", setting_data=settings_template)
def start(user_info):
    cache.deposit(id="user_info", data=user_info)
    cache.deposit(id="runtime", data=True)
    interface_loop()
def interface_loop():
    if cache.withdraw(id="runtime") == True:
        interface = settings.get_setting(id="interface")
        if interface == "gui":
            gui()
        elif interface == "cli":
            cl.home()
    else:
        quit()
    interface_loop()

def gui():
    class Api:
        def inteface(self,ui):
            window.load_html(fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/" + ui + ".ui")))
        def enc(self):
            mode = str(window.dom.get_element("#app-mode").value())
            if mode == "enc":
                file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=True, file_types=('All files (*.*)')))
            elif mode == "dec":
                file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=True, file_types=('All files (*.*)')))
            elif mode == "editor":
                file = list(window.create_file_dialog(webview.FileDialog.OPEN, allow_multiple=False, file_types=('Encrypted Files (*.encrypted)','All files (*.*)')))
                self.editor()
    def on_closed():
        cache.deposit(id="runtime", data=False)
        interface_loop()
    if __name__ == "__main__":
        api = Api()
        window = webview.create_window("Akari's Suite", html=fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/home.ui")), js_api=api, confirm_close=True)
        window.events.closed += on_closed
        webview.start()
    return

class cl:
    def home():
        cli.cls()
        cli.load_interface(name="main",index="home")
        x = int(input(" > "))
        if x == 0:
            cache.deposit(id="runtime", data=False)
            interface_loop()
    def enc():
        cli.cls()
        cli.load_interface(name="main", index="enc_0")
        x = int(input(" > "))
        if x == 0:
            cl.home()
        elif x == 1:
            cli.cls()
            cli.load_interface(name="main", index="enc_1")
            x = int(input(" > "))
            if x == 0:
                cl.enc()
            elif x == 1:
                cli.cls()
                cli.load_interface(name="main", index="enc_2")
                path = Path(input(" > "))
                cli.cls()
                cli.loader.start(data="Encrypting File... ")
                data = fc.open(path=path)
                user_info = cache.withdraw(id="user_info")
                data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
                fc.dump(data=data, path=path)
                cli.loader.succeed(data="Encrypted File Successfully! ")
                cli.wait(1)
                cl.enc()
            elif x == 2:
                cli.cls()
                cli.load_interface(name="main", index="enc_2_2")
                path = str(tkinter.filedialog.askopenfile())
                cli.cls()
                cli.loader.start(data="Encrypting File... ")
                data = fc.open(path=path)
                user_info = cache.withdraw(id="user_info")
                data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
                fc.dump(data=data, path=path)
                cli.loader.succeed(data="Encrypted File Successfully! ")
                cli.wait(1)
                cl.enc()
        elif x == 2:
            cli.cls()
            cli.load_interface(name="main", index="enc_1")
            x = int(input(" > "))
            if x == 0:
                cl.enc()
            elif x == 1:
                cli.cls()
                cli.load_interface(name="main", index="enc_2")
                path = Path(input(" > "))
                cli.cls()
                cli.loader.start(data="Decrypting File... ")
                data = fc.load(path=path)
                user_info = cache.withdraw(id="user_info")
                data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
                fc.write(data=data, path=path)
                cli.loader.succeed(data="Decrypted File Successfully! ")
                cli.wait(1)
                cl.enc()
            elif x == 2:
                cli.cls()
                cli.load_interface(name="main", index="enc_2_2")
                path = str(tkinter.filedialog.askopenfile())
                cli.cls()
                cli.loader.start(data="Decrypting File... ")
                data = fc.load(path=path)
                user_info = cache.withdraw(id="user_info")
                data = krypt.full_enc(username=user_info["username"], password=user_info["password"], data=data)
                fc.write(data=data, path=path)
                cli.loader.succeed(data="Decrypted File Successfully! ")
                cli.wait(1)
                cl.enc()