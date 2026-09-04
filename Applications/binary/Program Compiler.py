import os
import base64
import binascii
import Applications.binary.fc as fc
import Applications.binary.fb as fb
from Applications.binary.cachy import Cachy as cache
from pathlib import Path
import PyInstaller.__main__
class compiler:
    def set_python_id(id):
        cache.deposit(id="python_id", data=id)
        return

    def get_python_id():
        return cache.withdraw(id="python_id")

    def create_obfuscation_main(path):
        path = Path(path)
        python_id = compiler.get_python_id()
        os.system(python_id + ' -OO -m py_compile "' + path + '"')
        path_alt = Path(str(path).replace('.py', '.pyo'))
        path = Path(str(path).replace('.py', '_.py'))
        os.rename(path_alt, path)
        program = fc.open(path=path)
        program = base64.urlsafe_b64encode(program.encode())
        program = base64.b32encode(program)
        program = base64.b64encode(program)
        program = base64.urlsafe_b64encode(program.encode())
        program = program.decode()
        program = binascii.hexlify(program)
        template = """import base64
        import binascii
        program = '""" + program + """'
        program = binascii.unhexlify(program)
        program = base64.urlsafe_b64decode(program.encode())
        program = base64.b64decode(program)
        program = base64.b32decode(program)
        program = base64.urlsafe_b64decode(program)
        program = program.decode()
        eval(compile(program,'<string>','exec'))"""
        path_str = str(path)
        path_list = path.split('/')
        name = "runtime_" + str(path_list[-1])
        path_bade = path_str.replace(str(path_list[-1]), "runtime_" + str(path_list[-1]))
        path = Path(path_str)
        fc.touch(path=path)
        fc.write(path=path, data=template)
        return
    
    def obfuscate_file(path):
        path = Path(path)
        python_id = compiler.get_python_id()
        os.system(python_id + ' -OO -m py_compile "' + path + '"')
        path_alt = Path(str(path).replace('.py', '.pyo'))
        path = Path(str(path).replace('.py', '_.py'))
        os.rename(path_alt, path)
        return
    
    def obfuscate_modules(path):
        python_id = compiler.get_python_id()
        if not type(path) == list:
            path = list(path)
        for x in path:
            temp = Path(x)
            os.system(python_id + ' -OO -m py_compile "' + path + '"')
            path_alt = Path(str(path).replace('.py', '.pyo'))
            path = Path(str(path).replace('.py', '.pyc'))
        return
    
    def obfuscate_exe(path):
        path = Path(path)
        program = fc.open(path=path)
        program = base64.urlsafe_b64encode(program.encode())
        program = base64.b32encode(program)
        program = base64.b64encode(program)
        program = base64.urlsafe_b64encode(program.encode())
        program = program.decode()
        program = binascii.hexlify(program)
        template = """import base64
        import binascii
        program = '""" + program + """'
        program = binascii.unhexlify(program)
        program = base64.urlsafe_b64decode(program.encode())
        program = base64.b64decode(program)
        program = base64.b32decode(program)
        program = base64.urlsafe_b64decode(program)
        program = program.decode()
        eval(program,'<string>','exec')"""
        path_str = str(path)
        path_list = path.split('/')
        name = "runtime_" + str(path_list[-1])
        path_bade = path_str.replace(str(path_list[-1]), "runtime_" + str(path_list[-1]))
        path = Path(path_str)
        fc.touch(path=path)
        fc.write(path=path, data=template)
        return

    def compile_python(path, console=False, icon=None):
        if console == False:
            if icon == None:
                PyInstaller.__main__.run([path,'--onefile',''])
            elif icon != None:
                PyInstaller.__main__.run([path,'--onefile','--icon=' + icon])
        elif console == True:
            if icon == None:
                PyInstaller.__main__.run([path,'--onefile','--no-console'])
            elif icon != None:
                PyInstaller.__main__.run([path,'--onefile','--no-console','--icon=' + icon])
        return
