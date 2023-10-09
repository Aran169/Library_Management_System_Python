from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry('800x600+160+140')
root.title('BOOK MANAGEMENT SYSTEM')
mg=Image.open("E:/Arul murugan/Projects/Python/Project Snippets/x.jpg")
mg1=mg.resize((800,600))
img=ImageTk.PhotoImage(mg1)
xx=Label(image=img)
xx.pack()

def register():
    root.destroy()
    import register
def signup():
    root. destroy()
    import signup

Label=Label(root,text="LIBRARY MANAGEMENT SYSTEM",font=('Courier 20'),foreground="red")
Label.pack(side=TOP)
a=Button(root,text="SIGN UP",height= 2, width=9,command=signup)
a.pack()
a.place(x=360, y=210)
b=Button(root,text="REGISTER",height= 2, width=9,command=register)
b.pack()
b.place(x=360, y=290)
root.mainloop()
