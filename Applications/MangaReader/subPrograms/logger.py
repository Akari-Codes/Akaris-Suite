import os
from pathlib import Path
from datetime import datetime

Path(os.getcwd() + "/bin/logs/").mkdir(exist_ok=True,parents=True)
logsPath = os.getcwd() + "/bin/logs/"
fileName = datetime.datetime.now() + ".log"
currentLog = Path(logsPath + fileName)
global lineNum
lineNum = 0
global mode
mode = ""

def get_time():
    return datetime.strftime("%H:%M:%S")

def getLog():
    with open(currentLog, 'r') as f:
        return f.readlines()

def setLog(data):
    with open(currentLog, 'w') as f:
        f.writelines(data)
    return

def init(mode,appName):
    currentLog.touch()
    with open(currentLog, 'w') as f:
        f.write("[" + appName + " Logs]")
    mode = int(mode)
    print("Logger Is Online")
    return

def log(logData):
    logData = str(lineNum) + ": [" + str(get_time) + "] -  " + logData
    lineNum = lineNum + 1
    logs = getLog()
    logs.append(logData)
    setLog(data=logs)
    if mode == 0:
        return
    elif mode == 1:
        print(logData)
        return
    else:
        print("No mode has been selected please initilize logger!")
        return