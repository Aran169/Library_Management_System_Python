from tkinter import *
from PIL import Image, ImageTk
import time
import mysql.connector as mc
from tkinter import messagebox as ms
root=Tk()
root.title('return book')
root.geometry('800x600+160+140')
mg=Image.open("E:/Arul murugan/Projects/Python/Project Snippets/org image.jpg")
mg1=mg.resize((800,600))
img=ImageTk.PhotoImage(mg1)
xx=Label(image=img)
xx.pack()
def home():
    root.destroy()
    import home
def back():
    root.destroy()
    import LMS
def new():
    root.destroy()
    import newpage
def return_b():
    mydb = mc.connect(host="localhost",user="root",password="1234",database="lib")
    c = mydb.cursor()
    if book_id.get() != '' and n_reg.get()!= '':
        a1 = n_reg.get()
        b1 = book_id.get()
        c.execute(f'SELECT * FROM ab WHERE book_id = "{b1}" ')
        if c.fetchall() :
            dt=list(time.localtime())[:3]
            dt=[str(i) for i in dt]
            dt="-".join(dt)
            c.execute(f"update ss_ret set return_date='{dt}' where book_id='{b1}';")
            c.execute(f"update ss_ret set status='returned' where book_id='{b1}';")
            c.execute(f"update ab set reg_no=NULL where book_id='{b1}';")
            mydb.commit()
            ms.showinfo('book returned successfully')
        else:
            ms.showerror("Error!','The book is not available or invalid username.")
    else:
        ms.showerror('Error!','Please Enter the details.')
    mydb.close()
a=Button(root,text="HOME",height= 2, width=9,command=home)
a.pack()
a.place(x=30, y=30)
b=Button(root,text="BACK",height= 2, width=9,command=back)
b.pack()
b.place(x=130,y=30)
Book_id=Label(root,text="Reg.no:",bd=2,font=('Courier 13')).place(x=225,y=150)
Reg_No=Label(root,text="Book.id:",bd=2,font=('Courier 13')).place(x=235,y=200)
n_reg = StringVar()
book_id = StringVar()
e1=Entry(root,textvariable=n_reg,width=30,bd=3).place(x=350,y=150)
e2=Entry(root,textvariable=book_id,width=30,bd=3).place(x=350,y=200)
a=Button(root,text="RETURN",height= 2, width=9,command=return_b)
a.pack()
a.place(x=350, y=400)
root.mainloop()
