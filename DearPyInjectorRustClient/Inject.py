import dearpygui.dearpygui as x
from pymem.process import inject_dll #Injecting DLL
import pymem as p

class Injector:
    def InjectDLL(path: str):
        pymem_rust = p.Pymem("RustClient.exe")
        vbb = bytes(path)
        return inject_dll(pymem_rust.process_handle, vbb)
    def GetValue_Tag(tag: str):
        return x.get_value(tag)
    def CheckIfRustExists():
        pymnx = p.Pymem("RustClient.exe")
        if pymnx.process_id == 0:
            raise Exception("RustClient.exe is not Launched")