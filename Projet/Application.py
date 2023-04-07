import sys, math, time
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
from OpenGL import GL, GLU
from pyopengltk import OpenGLFrame

class Application:
    """"""

    def __init__(self, master):
        super().__init__()

        self.root = master

    def window(self):
        """ Method defining the window and it size
        """
        self.root.geometry("700x250")
        self.root.title("Wolfenstein version basique")

        




    def start(self):
        self.window()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.start()
