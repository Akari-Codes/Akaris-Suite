import cli
from cli import cls
import fc
import os
import sys
import cryptDome
import secrets
import time
import string
import yaml
import json
import pickle

pName = "swea"

def newDatabase():
    cls()
    print("[ Set Name for Database ]")
    print()
    dbName = str(input("Database Name > "))
    alphabet = string.ascii_letters + string.digits
    passphrase = ''.join(secrets.choice(alphabet) for i in range(20))
    cls()
    cli.load_reactive_interface(name=pName, index="databaseAdd",data_archive=[dbName,passphrase])
    dbPath = str(input("Database Path > "))
    dbTemplate = '''
[{user:"admin", passphrase:"AkariGames_VT6996"}]
'''
    cryptDome.encJs(data=[dbPath,dbTemplate,passphrase])
    time.sleep(1)
    return


def removeDatabase():
    cls()
    cli.load_interface(name=pName,index="databaseDel")
    dbPath = str(input("Dataase Path > "))
    fc.destroy(path=dbPath)
    time.sleep(1)
    return

def addUser():
    cls()
    cli.load_reactive_interface(name=pName,index="databaseEdit", data_archive=["add"])
    dbPath = str(input("Database Path > "))
    print()
    print("[ Set Name for User ]")
    print()
    username = str(input("Username > "))
    cls()
    cli.load_reactive_interface(name=pName, index="userAdd", data_archive=[dbPath,username])
    password = str(input("Password > "))
    db = json.loads(cryptDome.decJs([dbPath,password], save=False))
    db.append('''{"user":"''' + username + '''", "passphrase":"''' + password + '''"}''')
    db = json.dump(db)
    db = str(db)
    cryptDome.encJs([dbPath,db,password])
    return


def removeUser():
    cls()
    cli.load_reactive_interface(name=pName,index="databaseEdit", data_archive=["delete"])
    dbPath = str(input("Database Path > "))
    cli.load_reactive_interface(name=pName, index="userDel",data_archive=[dbPath])
    username = str(input("Username > "))
    

def start():
    cls()
    cli.load_interface(name=pName,index="index")
    q = int(input(" > "))
    if q == 1:
        addUser()
    elif q == 2:
        removeUser()
    elif q == 3:
        newDatabase()
    elif q == 4:
        removeDatabase()
start()