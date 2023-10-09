import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector as mc
win=Tk()
win.title('AVAILABILITY')
win.geometry('800x600+160+140')
def back():
    win.destroy()
    import LMS
style = ttk.Style()
style.theme_use('clam')

mydb = mc.connect(host="localhost",user="root",password="1234",database="lib")
c = mydb.cursor()
c.execute("select * from ab where reg_no is NULL;")
lst=[i for i in c]
print(lst)
mydb.close()

tree = ttk.Treeview(win, column=( " book_id","book_name","author"), show='headings', height=5)
tree.column("# 1", width=100,anchor=CENTER)
tree.heading("# 1", text="book_id")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="book_name ")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="author")
b=Button(win,text="BACK",height= 2, width=9,command=back)
b.pack()
b.place(x=30, y=30)

for i in range(len(lst)):
    
    tree.insert('', 'end', text="1", values=lst[i])
               
tree.pack()
win.mainloop()
