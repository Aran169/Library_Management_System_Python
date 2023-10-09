import tkinter
from tkinter import *
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import mysql.connector as mc
window=Tk()

window.geometry('800x600+160+140')
mg=Image.open("E:/Arul murugan/Projects/Python/Project Snippets/x2.jpg")
mg1=mg.resize((800,600))
img=ImageTk.PhotoImage(mg1)
xx=Label(image=img)
xx.pack()
window.title('SIGNUP')
width=700
height=500
x=60
y=40
window.geometry('800x600+160+140')
def home():
    window.destroy()
    import home
def signup():
    
    a,b=username.get(),password.get()
    mydb = mc.connect(host="localhost",user="root",passwd="1234",database="lib")
    c = mydb.cursor()
    print(a,b)
    if a != '' and b!= '':
        # Find the correct user
        find_user = (f'SELECT * FROM user1 WHERE user= %s and password = %s')
        c.execute(find_user, [(a), (b)])
        result = c.fetchall()
        if result:
            window.destroy()
            import LMS
        else:
            ms.showerror('Oops!', 'Check the username or password again.')
    else:
        ms.showerror('Error!', 'Please Enter the details.')
    mydb.close()
    
#def validateLogin(username, password):
	
username=Label(window,text="Username : ",bd=2,font=('Courier 13')).place(x=225,y=170)
username = StringVar()
password=Label(window,text="Password : ",bd=2,font=('Courier 13')).place(x=225,y=230)
password = StringVar()
e1=Entry(window,textvariable=username,width=30).place(x=350,y=170)
e2=Entry(window,textvariable=password,width=30).place(x=350,y=230)
a=Button(window,text="SIGN UP",height= 2, width=15,command=signup)
a.pack()
a.place(x=340,y=290)
b=Button(window,text="HOME",height= 2, width=15, command=home)
b.pack()
b.place(x=30,y=30)

window.mainloop()
