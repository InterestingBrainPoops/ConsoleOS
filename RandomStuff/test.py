# Probably never going to be used in  the current implementation, but allows me to display files in a tkinter text widget.

import tkinter as tk 
import sys
f = open("README.md", "r")
filecontents = f.read()
f.close()
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=file_len("README.md"), width=50) #replace file_len("README.md") w/ the height that you want (in lines)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = filecontents
T.insert(tk.END, quote)
tk.mainloop()

