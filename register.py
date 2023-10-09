import tkinter
from tkinter import *
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import mysql.connector as mc

window=Tk()
window.geometry('800x600+160+140')
mg=Image.open("E:/Arul murugan/Projects/Python/Project Snippets/library photo.jpg")
mg1=mg.resize((800,600))
img=ImageTk.PhotoImage(mg1)
xx=Label(image=img)
xx.pack()
window.title('Register')
width=700
height=500
x=60
y=40
window.geometry('800x600+160+140')
def new():
    a3,b3,c3,d3,p1=a2.get(),b2.get(),c2.get(),d2.get(),p.get()
    
    mydb = mc.connect(host="localhost",user="root",passwd="1234",database="lib")
    c = mydb.cursor()
    print(a,b)
    if a3 != '' and b3!= '' and c3 != '' and d3!= '' and e3 != '':
        # Find the correct user
        #print(a3,b3,c3,d3,p3)
        
        find_user = (f"insert into user1 values(%s,%s,%s,%s,%s);")
        c.execute(find_user, [(a3), (b3), (c3), (d3), (p1)])
        mydb.commit()
        mydb.close()
        window.destroy()
        import signup
    else:
        ms.showerror('Error!', 'Please Enter the details.')
def home():
    window.destroy()
    import home
First_name=Label(window,text="First Name:",bd=2,font=('Courier 13')).place(x=225,y=150)
Last_name=Label(window,text="Last Name:",bd=2,font=('Courier 13')).place(x=235,y=200)
reg_no=Label(window,text="Reg_number:",bd=2,font=('Courier 13')).place(x=225,y=250)
user_id=Label(window,text="user id:",bd=2,font=('Courier 13')).place(x=250,y=300)
passw=Label(window,text="Password:",bd=2,font=('Courier 13')).place(x=240,y=350)
a2,b2,c2,d2,p=StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
e1=Entry(window,textvariable=a2,width=30,bd=3).place(x=350,y=150)
e2=Entry(window,textvariable=b2,width=30,bd=3).place(x=350,y=200)
e3=Entry(window,textvariable=c2,width=30,bd=3).place(x=350,y=250)
e4=Entry(window,textvariable=d2,width=30,bd=3).place(x=350,y=300)
e5=Entry(window,textvariable=p,width=30,bd=3).place(x=350,y=350)
a=Button(window,text="REGISTER",height= 2, width=9,command=new)
b=Button(window,text="HOME",height= 2, width=9,command=home)
a.pack()
a.place(x=350, y=400)
b.pack()
b.place(x=30, y=30)
window.mainloop()
