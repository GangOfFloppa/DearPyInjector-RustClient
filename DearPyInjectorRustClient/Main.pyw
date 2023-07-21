import Window as w
import tkinter.messagebox as msg
import Inject as x_inject

def WelcomeBox():
    return msg.showinfo(title="DearPyInjector", message="Welcome to my New Injector for Game RustClient")
def MainThread():
    WelcomeBox()
    w.Window.MainWindow()
if __name__ == "__main__":
    x_inject.Injector.CheckIfRustExists()
    MainThread()
