import base64
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from pathlib import Path
def kdf(password: bytes, salt: bytes, key_len=32, iv_len=16):
    derived = b""
    last_block = b""
    while len(derived) < (key_len + iv_len):
        last_block = md5(last_block + password + salt).digest()
        derived += last_block
    return derived[:key_len], derived[key_len:key_len + iv_len]
def enc_f(plaintext: str, passphrase: str):
    password_bytes = passphrase.encode('utf-8')
    salt = get_random_bytes(8)
    key, iv = kdf(password_bytes, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    openssl_format = b"Salted__" + salt + ciphertext
    b64_output = base64.b64encode(openssl_format)
    return b64_output
def dec_f(b64_data: str, passphrase: str) -> str:
    encrypted_data = base64.b64decode(b64_data)
    if encrypted_data[:8] != b"Salted__":
        raise ValueError("Invalid format: Missing CryptoJS 'Salted__' prefix.")
    salt = encrypted_data[8:16]
    ciphertext = encrypted_data[16:]
    password_bytes = passphrase.encode('utf-8')
    key, iv = kdf(password_bytes, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded, AES.block_size).decode('utf-8')
    return plaintext
def encJs(data=["dest-path","data-to-encrypt","passphrase"], save=True):
    if save == True:
        Path(data[0]).touch()
        with open(Path(data[0]), 'wb') as f:
            f.write(enc_f(data[1], data[2]))
        return
    else:
        return enc_f(data[1], data[2])
def decJs(data=["src-path", "passphrase","dest-path"], save=True):
    with open(Path(data[0],'r')) as f:
        data.append(f.read())
    if save == True:
        Path(data[2]).touch()
        with open(Path(data[2], 'w')) as f:
            f.write(dec_f(data[3], data[1]))
        return
    else:
        return dec_f(data[3], data[1])