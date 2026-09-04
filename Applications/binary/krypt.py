from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def full_enc(password, data):
    password = base64.urlsafe_b64decode(password)
    password = base64.b16decode(password)
    password = base64.b32hexdecode(password)
    password = base64.a85decode(password)
    password = base64.urlsafe_b64decode(password)
    password = password.decode()
    salt = 696912345678901234567890098765432109876543216969
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=256,salt=salt,iterations=100_000,)
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    key = pass_key
    f = Fernet(key)
    data = base64.urlsafe_b64encode(data.encode())
    data = base64.a85encode(data)
    data = base64.b32hexencode(data)
    data = base64.urlsafe_b64encode(data)
    data = f.encrypt(data)
    data = base64.urlsafe_b64encode(data)
    data = base64.b64encode(data)
    data = base64.b32encode(data)
    data = base64.b85encode(data)
    data = base64.standard_b64encode(data)
    data = base64.urlsafe_b64encode(data)
    data = f.encrypt(data)
    data = base64.urlsafe_b64encode(data)
    data = base64.b64encode(data)
    data = base64.b32encode(data)
    data = base64.b85encode(data)
    data = base64.standard_b64encode(data)
    data = base64.urlsafe_b64encode(data)
    data = base64.a85encode(data)
    data = base64.b32hexencode(data)
    data = base64.urlsafe_b64encode(data)
    data = f.encrypt(data)
    data = base64.urlsafe_b64encode(data)
    data = data.decode()
    return data

def new_pass(password):
    password = base64.urlsafe_b64encode(password.encode())
    password = base64.a85encode(password)
    password = base64.b16encode(password)
    password = base64.b32hexencode(password)
    password = base64.urlsafe_b64encode(password)
    return password

def full_dec(password, data):
    password = base64.urlsafe_b64decode(password)
    password = base64.b16decode(password)
    password = base64.b32hexdecode(password)
    password = base64.a85decode(password)
    password = base64.urlsafe_b64decode(password)
    password = password.decode()
    salt = 696912345678901234567890098765432109876543216969
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=256,salt=salt,iterations=100_000,)
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    key = password
    f = Fernet(key)
    data = base64.urlsafe_b64decode(data.encode())
    data = f.decrypt(data)
    data = base64.urlsafe_b64decode(data)
    data = base64.b32hexdecode(data)
    data = base64.a85decode(data)
    data = base64.urlsafe_b64decode(data)
    data = base64.standard_b64decode(data)
    data = base64.b85decode(data)
    data = base64.b32decode(data)
    data = base64.b64decode(data)
    data = base64.urlsafe_b64decode(data)
    data = f.decrypt(data)
    data = base64.urlsafe_b64decode(data)
    data = base64.standard_b64decode(data)
    data = base64.b85decode(data)
    data = base64.b32decode(data)
    data = base64.b64decode(data)
    data = base64.urlsafe_b64decode(data)
    data = f.decrypt(data)
    data = base64.urlsafe_b64decode(data)
    data = base64.b32hexdecode(data)
    data = base64.a85decode(data)
    data = base64.urlsafe_b64decode(data)
    data = data.decode()
    return data
