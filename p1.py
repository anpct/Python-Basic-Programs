import cx_Oracle
import tkinter as tk
from tkinter import ttk
def one(e1,e2):
    c.execute("insert into hr.a values('{}','{}')".format(e1,e2))
    c.execute("commit")
def two():
    tree.delete(*tree.get_children())
    c.execute("Select * from hr.a")
    for row in c:
        tree.insert("", 0, text=row[0], values=(row[1]))
if __name__=="__main__":
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
    conn = cx_Oracle.connect(user='system', password='Anoop1998', dsn=dsn_tns)
    c = conn.cursor()
    c.execute("alter session set container=orclpdb ")
    mainpage = tk.Tk()
    nb = ttk.Notebook(mainpage)
    t1 = ttk.Frame(nb)
    t2 = ttk.Frame(nb)
    nb.add(t1, text="INSERT")
    nb.add(t2, text="SELECT")
    l1 = tk.Label(t1, text="ID")
    e1 = tk.Entry(t1)
    l2 = tk.Label(t1, text="NAME")
    e2 = tk.Entry(t1)
    b1 = tk.Button(t1, text="ADD", command=lambda : one(e1.get(),e2.get()))
    l1.grid()
    e1.grid()
    l2.grid()
    e2.grid()
    b1.grid()
    b2 = tk.Button(t2, text="DISPLAY", command=lambda: two())
    tree = ttk.Treeview(t2)
    tree["columns"] = ("one")
    tree.heading("#0", text="ID")
    tree.heading("one", text="Name")
    b2.pack()
    tree.pack()
    b2.pack()
    nb.pack()
    mainpage.mainloop()

