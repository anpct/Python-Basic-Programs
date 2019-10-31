import cx_Oracle
import tkinter as tk
from tkinter import ttk
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
conn = cx_Oracle.connect(user='system', password='Anoop1998', dsn=dsn_tns)
c = conn.cursor()
c.execute('alter session set container=orclpdb')
c.execute('SELECT * FROM hr.EMPLOYEES')
master=tk.Tk()
tree=ttk.Treeview(master)
tree["columns"]=("one")
tree.heading("#0", text="ID")
tree.heading("one", text="Name")
for row in c:
    tree.insert("",0,text=row[0],values=(row[1]))
tree.pack()
master.mainloop()
conn.close()
