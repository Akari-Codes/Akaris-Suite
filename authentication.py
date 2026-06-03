import fb
import fc
from cachy import Cachy as cache
import os
import webview
from webview import *
import settings
import krypt
import main
import time

settings_template = {
    {"remember_user":False}
    }
settings.init(name="auth", settings_data=settings_template)

class auth:
    def login_gui(window, username, password):
        window.dom.get_element('#l1').text = "Logging into Account..."
        if krypt.pass_check(username, password) == True:
            user_info = krypt.get_user_info(user_path=str(os.getcwd() + "/bin/users/" + username + "/"))
            time.sleep(1)
            window.dom.get_element('#l1').text = "Logging into Account - Completed /"
            time.sleep(1)
            window.hide()
            window.destroy()
            main.start(user_info)
        else:
            window.dom.get_element('#l1').text = "Login Failed!!!"
            time.sleep(1)
            window.load_html(fc.open(path=os.getcwd() + "/bin/ui/graphical/auth.ui"))
            return

    def register_gui(window, username, password, s_pin):
        krypt.new_user(username, password, s_pin)
        window.dom.get_element('#l2').text = "Creating Account - Completed /"
        window.dom.get_element('#l1').text = "Processing Details - Completed /"
        time.sleep(1)
        window.dom.get_element('#l1').text = ""
        window.dom.get_element('#l2').text = ""
        auth.login_gui(username, password)
        return
def gui():
    class Api:
        def interface(self, ui):
            window.load_html(fc.open(path=os.getcwd() + "/bin/ui/graphical/" + ui + ".ui"))
            return
        def login(self):
            username = str(window.dom.get_element('#username').value)
            password = str(window.dom.get_element('#password').value)
            if auth.check_pass(username, password) == True:
                auth.login(window, username, password)
            else:
                window.dom.get_element('#l_error').text = "Failed to Login Username or Password is Incorrect!!"
        def signup(self):
            fail = False
            username = str(window.dom.get_element('#username').value)
            password = str(window.dom.get_element('#password').value)
            c_password = str(window.dom.get_element('#c_password').value)
            try:
                s_pin = int(window.dom.get_element('#s_pin').value)
            except:
                fail = True
                window.dom.get_element('#s_pin_error').text = "Security Pin is not Valid - Incorrect Format Pin Must be Numbers!!"
            if username == "":
                fail = True
                window.dom.get_element('#username_error').text = "Username is not Valid!!"
            if not password == c_password:
                fail = True
                window.dom.get_element('#c_password_error').text = "Passwords do not match!!"
            if fail == False:
                self.interface("loader_light")
                window.dom.get_element('#l1').text = "Processing Details..."
                window.dom.get_element('#l2').text = "Creating Account..."
                auth.register(window, username,password,s_pin)
    if __name__ == "__main__":
        api = Api()
        window = webview.create_window("Authentication", html=fc.open(path=os.getcwd() + "/bin/ui/graphical/auth.ui"),js_api=api)
        webview.start()
gui()