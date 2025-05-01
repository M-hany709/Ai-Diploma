from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from novels import open_root_novels
from children import open_root_children
from Religious import open_root_Religious
from Political import open_root_Political
from Psychology_socioty import open_root_Psychology_socioty
from mylibrary import open_root_mylibrary



root=Tk()
root.attributes("-fullscreen", True)
root.title("Library system mangement")
root.configure(bg="#d8d9ff")
root.resizable(False,False)
l=Label(root,text="Library system mangement",fg="#b8860b",bg="#d8d9ff",font=("Arail",28,"bold"))
l.pack(pady=50)

def open_root3():
    root3=Toplevel()
    root3.attributes("-fullscreen", True)
    root3.title("Kinds of Books")
    root3.resizable(False,False)
    root3.configure(bg="white")
    l=Label(root3,text="          Main Library          ",font=("Arial",28,"bold"),fg="#b8860b" , bg="#d8d9ff")
    l.pack(pady=50)
    b1=Button(root3,text="Novels",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root_novels,width="23",height="2")
    b1.place(x=400,y=300)
    b2=Button(root3,text="Psychology & socioty",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root_Psychology_socioty,width="23",height="2")
    b2.place(x=900,y=300)
    b3=Button(root3,text="Political",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root_Political,width="23",height="2")
    b3.place(x=400,y=450)
    b4=Button(root3,text="Religious",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root_Religious,width="23",height="2")
    b4.place(x=900,y=450)
    b5=Button(root3,text="For childern",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root_children,width="23",height="2")
    b5.place(x=650,y=600)
    bpack=Button(root3,text="pack",command=root3.destroy ,font=("Arial",28,"bold"),fg="#b8860b" , bg="#1e213f",width=10,height=1)
    bpack.place(x=0,y=750)
#*******************************************************************************************************************************************************************************************************

b1=Button(root,text="my library",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root_mylibrary,width="20",height="10")
b1.place(x=400,y=300)
b2=Button(root,text="Main library",fg="#b8860b",bg="#1e213f",font=("Arial",20,"bold"),command=open_root3,width="20",height="10")
b2.place(x=900,y=300)

root.mainloop()

