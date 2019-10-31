# Python program to demonstrate working with a GUI environment


import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')
tabControl.pack(expand=1, fill="both")
btn = tk.Button(tab1, text='PRESS', command=win.destroy)
btn.pack()
ck=tk.Radiobutton(tab2, text='click')
ck.pack()
ntr=tk.Entry(tab3)
ntr.pack()
l=tk.Label(tab3, text=ntr.get())
l.pack()
win.mainloop()