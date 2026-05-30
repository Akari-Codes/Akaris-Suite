import fb
import fc
from cachy import Cachy as cache
import os
import webview
from webview import *
import settings
import cli
import krypt
import main
settings_template = {
    {"interface_mode":"gui"},
    {"remember_user":False},
    }
settings.init(name="auth", settings_data=settings_template)
class auth:
    def login(username, password):
        if krypt.pass_check(username, password) == True:
            user_info = krypt.get_user_info(user_path=str(os.getcwd() + "/bin/users/" + username + "/"))
            main.start(user_info)
    def register(username, password, s_pin):
        krypt.new_user(username, password, s_pin)
        auth.login(username, password)
def gui():
    class Api:
        def interface(self, ui):
            window.load_html(fc.open(path=os.getcwd() + "/bin/ui/graphical/" + ui + ".ui"))
            return
        def login(self):
            username = str(window.dom.get_element('#username').value)
            password = str(window.dom.get_element('#password').value)
            if auth.check_pass(username, password) == True:
                auth.login(username, password)
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
                window.dom.get_element('c_password_error').text = "Passwords do not match!!"
            if fail == False:
                self.interface("auth-processing")
                auth.register(username,password,s_pin)
    if __name__ == "__main__":
        api = Api()
        window = webview.create_window("Authentication", html=fc.open(path=os.getcwd() + "/bin/ui/graphical/" + "auth" + ".ui"),js_api=api)
        webview.start()
class cl:
    def auth():
        cli.cls()
        cli.load_interface(name="auth",index="auth")
        i = int(input(" > "))
        if i == 0:
            quit()
        elif i == 1:
            cl.login()
        elif i == 2:
            cl.signup()
        else:
            cl.auth()
    def login():
        cli.load_interface(name="auth",index="login")
        username = input(" > ")
        print()
        print("Enter Password:")
        print()
        password = input(" > ")
        cli.cls()
        cli.loader.start(data="Processing Details... ")
        if auth.check_pass(username, password) == True:
            auth.login(username, password)
        else:
            cli.loader.fail(data="Details are Incorrect!! ")
            cli.sleep(1)
            cl.login()
    def signup():
        cli.load_interface(name="auth",index="signup")
        username = input(" > ")
        print()
        print("Set Password:")
        print()
        password = input(" > ")
        print()
        print("Confirm Password:")
        print()
        c_password = input(" > ")
        print()
        print("Set Security Pin:")
        print()
        s_pin = int(input(" > "))
        cli.cls()
        cli.loader.start(data="Processing Details... ")
        if password == c_password:
            auth.signup(username, password, s_pin)
        else:
            cli.loader.fail(data="Details are not Valid!! ")
            cli.sleep(1)
            cl.signup()
if settings.get_setting(id="interface_mode") == "gui":
    gui()
elif settings.get_setting(id="interface_mode") == "cli":
    cl.auth()
else:
    quit()