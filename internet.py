from tkinter import *
from tkinter import ttk

import os

def perevesti():
    os.system('start r.py')
    import sys
    sys.exit
    
def ne_perevesti():
    os.system('start e.py')
    import sys
    sys.exit
    



root = Tk()
root.title("i")
root.geometry("200x100")
root.resizable(width=500,height=500)
btn1 = ttk.Button(text="русская версия", command=perevesti)
btn1.pack(anchor="nw",padx=0, pady=0)
btn1 = ttk.Button(text="english version", command=ne_perevesti)
btn1.pack(anchor="nw",padx=0, pady=0)
root.mainloop()