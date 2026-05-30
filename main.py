from cachy_sub import Cachy as cache
import os
import fc
import fb
import crypt
import settings
import webview
import cli
settings_template = {
    {"interface":"gui"}
}
settings.init(name="main", setting_data=settings_template)
def start(user_info):
    cache.deposit(id="user_info", data=user_info)
    cache.deposit(id="runtime", data=True)
    def interface_loop():
        if cache.withdraw(id="runtime") == True:
            interface = settings.get_setting(id="interface")
            if interface == "gui":
                gui()
            elif interface == "cli":
                cl.home()
        else:
            return
        interface_loop()
    interface_loop()

def gui():
    class Api:
        def inteface(ui):
            window.load_html(fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/" + ui + ".ui")))
    if __name__ == "__main__":
        api = Api()
        window = webview.create_window("Akari's Suite", html=fc.open(path=str(os.getcwd() + "/bin/ui/graphical/main/home.ui")), js_api=api)
        webview.start()
    return
    
class cl:
    def home():
        cli.load_interface(name="main",index="home")