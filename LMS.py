import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window=Tk()
window.geometry('800x600+160+140')
mg=Image.open("E:/Arul murugan/Projects/Python/Project Snippets/org image.jpg")
mg1=mg.resize((800,600))
img=ImageTk.PhotoImage(mg1)
xx=Label(image=img)
xx.pack()
window.title('LMS')
width=700
height=500
x=60
y=40
window.geometry('800x600+160+140')
def home():
    window.destroy()
    import home
def back():
    window.destroy()
    import signup
def avail():
    window.destroy()
    import availablebooks
def issue():
    window.destroy()
    import issuebooks
def returnbooks():
    window.destroy()
    import returnbooks
a=Button(window,text="HOME",height= 2, width=9,command=home)
a.pack()
a.place(x=30, y=30)
b=Button(window,text="BACK",height= 2, width=9,command=back)
b.pack()
b.place(x=130, y=30)
c=Button(window,text="AVAILABLE BOOKS",height= 3, width=20,bd=3,command=avail)
c.pack()
c.place(x=340,y=200)
d=Button(window,text="RETURN BOOK",height= 3, width=20,bd=3,command=returnbooks)
d.pack()
d.place(x=340,y=280)
e=Button(window,text="ISSUE BOOK",height= 3, width=20,bd=3,command=issue)
e.pack()
e.place(x=340,y=360)
window.mainloop()
