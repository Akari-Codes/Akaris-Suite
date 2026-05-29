import os
from pathlib import Path
import joblib
import shutil
def touch(path, multi=False):
    if multi == True:
        for x in len(path)-1:
            Path(str(path)).touch(exist_ok=True)
    else:
        Path(str(path)).touch(exist_ok=True)
    return
def open(path, multi=False):
    if multi == False:
        with Path(str(path)) as fc:
            data = fc.read_text()
    else:
        data = []
        for x in path:
            with Path(x) as fc:
                data.appened(fc.read())
    return data
def open_bytes(path, multi=False):
    if multi == False:
        with Path(str(path)) as fc:
            data = fc.read_bytes()
    else:
        data = []
        for x in path:
            with Path(str(x)) as fc:
                data.appened(fc.read_bytes())
    return data
def write(data, path, multi=False):
    if multi == True:
        c = 0
        for x in path:
            c += 1
            with Path(str(x)) as fc:
                fc.write_text(data[c])
    else:
        with Path(str(path)) as fc:
            fc.write_text(data)
    return
def write_bytes(data, path, multi=False):
    if multi == True:
        c = 0
        for x in len(path)-1:
            c += 1
            with Path(str(x)) as fc:
                fc.write_bytes(data[c])
    else:
        with Path(str(path)) as fc:
            fc.write_bytes(data)
    return
def load(path):
    data = joblib.load(Path(str(path)))
    return data
def dump(data, path, multi=False):
    joblib.dump(data, Path(str(path)))
    return
def destroy(path, multi=False):
    if multi == True:
        for x in path:
            os.remove(Path(str(x)))
    else:
        os.remove(Path(str(path)))
    return
def move(src, dest, multi=False):
    if multi == True:
        for x in len(src)-1:
            shutil.move(Path(str(src[x])), Path(str(dest[x])))
    else:
        shutil.move(Path(str(src)), Path(str(dest)))
    return
def copy(src, dest, multi=False):
    if multi == True:
        for x in len(src)-1:
            shutil.copy(Path(str(src[x])), Path(str(dest[x])))
    else:
        shutil.copy(Path(str(src)), Path(str(dest)))
    return
def exists(path, multi=False):
    if multi == False:
        if Path(str(path)).exists():
            data = True
        else:
            data = False
    else:
        data = []
        for x in path:
            if Path(str(x)).exists():
                data.append(True)
        else:
            data.append(False)
    return data
def mkdir(path, multi=False):
    if multi == False:
        if Path(path).is_dir():
            Path(path).mkdir(exist_ok=True,parents=True)
    else:
        for x in path:
            if Path(x).is_dir():
                Path(x).mkdir(exist_ok=True,parents=True)
    return
def get_zero_map(filed):
      bytes = int(os.path.getsize(filed))
      bits = int(bytes) / int(8)
      count = 0
      zero_map = ""
      while int(bits) > count:
         count += 1
         zero_map += "0b0"
      return zero_map
def erase(path="", paths=[], multi=False):
      if multi == False:
        filed = Path(path)
        print("Erasing File: " + str(filed))
        joblib.dump(erase.get_zero_map(filed), filed)
        os.remove(filed)
        print("File Erased: " + str(filed))
      else:
        print("Erasing Files... This may take a while.")
        print("Files to be Erased: " + str(paths))
        for x in paths:
            single_erase.file(path=x)
      return
def single_erase(path):
    filed = Path(path)
    print("Erasing File: " + str(filed))
    joblib.dump(erase.get_zero_map(filed), filed)
    os.remove(filed)
    print("File Erased: " + str(filed))
    return