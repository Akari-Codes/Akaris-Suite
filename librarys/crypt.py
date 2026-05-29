from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
import fc
import os
import pickle
import random
def get_key_user(username):
    if fc.exists(path=str(os.getcwd() + "/bin/users/keys/" + username + ".dat")) == True:
        key = fc.load(path=str(os.getcwd() + "/bin/users/keys/" + username + ".dat"))
    else:
        key = "error"
    return key
def set_key_user(username, key):
    fc.mkdir(path=str(os.getcwd() + "/bin/users/keys/"))
    fc.touch(path=str(os.getcwd() + "/bin/users/keys/" + username + ".dat"))
    fc.dump(data=key, path=str(os.getcwd() + "/bin/users/keys/" + username + ".dat"))
    return
def set_user_info(user_info, user_path):
    fc.mkdir(path=user_path)
    fc.touch(user_path + "user.dll")
    fc.dump(data=user_info, path=user_path + "user.dll")
    return
def get_user_info(user_path):
    user_info = fc.load(path=user_path + "user.dll")
    user_info = pickle.loads(user_info)
    return user_info

def full_enc(username, password, data):
    password = base64.urlsafe_b64encode(password.encode())
    password = base64.a85encode(password)
    password = base64.b16encode(password)
    password = base64.b32hexencode(password)
    password = base64.urlsafe_b64encode(password)
    user_info = get_user_info(user_path=str(os.getcwd() + "/bin/users/" + username + "/"))
    salt = user_info["sap"]
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=256,salt=salt,iterations=100_000,)
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(pass_key)
    s_pin = f.decrypt(s_pin)
    s_pin = base64.urlsafe_b64decode(s_pin)
    s_pin = base64.b32hexdecode(s_pin)
    s_pin = base64.b16decode(s_pin)
    s_pin = base64.a85decode(s_pin)
    s_pin = base64.urlsafe_b64decode(s_pin)
    s_pin = f.decrypt(s_pin)
    s_key = base64.urlsafe_b64encode(kdf.derive(s_pin))
    f = Fernet(s_key)
    key = get_key_user(username)
    key = f.decrypt(key)
    key = base64.urlsafe_b64decode(key)
    key = base64.b32hexdecode(key)
    key = base64.b16decode(key)
    key = base64.a85decode(key)
    key = base64.urlsafe_b64decode(key)
    f = Fernet(key)
    data = base64.urlsafe_b64encode(data.encode())
    data = base64.a85encode(data)
    data = base64.b16encode(data)
    data = base64.b32hexencode(data)
    data = base64.urlsafe_b64encode(data)
    data = f.encrypt(data)
    data = base64.urlsafe_b64encode(data)
    data = base64.b64encode(data)
    data = base64.b32encode(data)
    data = base64.b85encode(data)
    data = base64.standard_b64encode(data)
    data = base64.urlsafe_b64decode(data)
    data = f.encrypt(data)
    data = base64.urlsafe_b64encode(data)
    data = base64.b64encode(data)
    data = base64.b32encode(data)
    data = base64.b85encode(data)
    data = base64.standard_b64encode(data)
    data = base64.urlsafe_b64decode(data)
    data = base64.a85encode(data)
    data = base64.b16encode(data)
    data = base64.b32hexencode(data)
    data = base64.urlsafe_b64encode(data)
    data = f.encrypt(data)
    data = base64.urlsafe_b64encode(data)
    return data
    

def full_enc_new(username, password, s_pin):
    password = base64.urlsafe_b64encode(password.encode())
    password = base64.a85encode(password)
    password = base64.b16encode(password)
    password = base64.b32hexencode(password)
    password = base64.urlsafe_b64encode(password)
    salt = random.randint(1, 99999999999)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=256,salt=salt,iterations=100_000,)
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(pass_key)
    o_s_pin = s_pin
    s_pin = f.encrypt(s_pin.encode())
    s_pin = base64.urlsafe_b64encode(s_pin)
    s_pin = base64.a85encode(s_pin)
    s_pin = base64.b16encode(s_pin)
    s_pin = base64.b32hexencode(s_pin)
    s_pin = base64.urlsafe_b64encode(s_pin)
    s_pin = f.encrypt(s_pin)
    o_s_key = base64.urlsafe_b64encode(kdf.derive(o_s_pin))
    s_key = base64.urlsafe_b64encode(kdf.derive(s_pin))
    f = Fernet(s_key)
    key = f.encrypt(password)
    key = base64.urlsafe_b64encode(key)
    key = base64.a85encode(key)
    key = base64.b16encode(key)
    key = base64.b32hexencode(key)
    key = base64.urlsafe_b64encode(key)
    f = Fernet(o_s_key)
    key = f.encrypt(key)
    key = base64.urlsafe_b64encode(key)
    key = base64.a85encode(key)
    key = base64.b16encode(key)
    key = base64.b32hexencode(key)
    key = base64.urlsafe_b64encode(key)
    set_key_user(username, key)
    user_info = {{"password":password},{"s_pin":s_pin}, {"sap":salt}}
    set_user_info(user_info, user_path=str(os.getcwd() + "/bin/users/" + username + "/"))
    return
def full_dec(username, password):
    password = base64.urlsafe_b64encode(password.encode())
    password = base64.a85encode(password)
    password = base64.b16encode(password)
    password = base64.b32hexencode(password)
    password = base64.urlsafe_b64encode(password)
    user_info = get_user_info(user_path=str(os.getcwd() + "/bin/users/" + username + "/"))
    salt = user_info["sap"]
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=256,salt=salt,iterations=100_000,)
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(pass_key)
    s_pin = f.decrypt(s_pin)
    s_pin = base64.urlsafe_b64decode(s_pin)
    s_pin = base64.b32hexdecode(s_pin)
    s_pin = base64.b16decode(s_pin)
    s_pin = base64.a85decode(s_pin)
    s_pin = base64.urlsafe_b64decode(s_pin)
    s_pin = f.decrypt(s_pin)
    s_key = base64.urlsafe_b64encode(kdf.derive(s_pin))
    f = Fernet(s_key)
    key = get_key_user(username)
    key = f.decrypt(key)
    key = base64.urlsafe_b64decode(key)
    key = base64.b32hexdecode(key)
    key = base64.b16decode(key)
    key = base64.a85decode(key)
    key = base64.urlsafe_b64decode(key)
    
def pass_check(username, password):
    key = get_key_user(username)
    if key == "error":
        return False
    user_path = str(os.getcwd() + "/bin/users/" + username + "/")
    if fc.exists(path=user_path) == True:
        user_info = get_user_info(user_path)
        password = base64.urlsafe_b64encode(password.encode())
        password = base64.a85encode(password)
        password = base64.b16encode(password)
        password = base64.b32hexencode(password)
        password = base64.urlsafe_b64encode(password)
        if password == user_info["password"]:
            return True
        else:
            return False
    else:
        return False