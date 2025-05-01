from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db_Psychology_socioty import librarys
from mylibrary import add_book

db_Psychology_socioty=librarys("booksPsychology_socioty.db")


def open_root_Psychology_socioty():
    rootPsychology_socioty=Toplevel()
    rootPsychology_socioty.attributes("-fullscreen", True)
    rootPsychology_socioty.title("Library system mangement")
    rootPsychology_socioty.resizable(False,False)
    rootPsychology_socioty.configure(bg="#d8d9ff")
    l=Label(rootPsychology_socioty,text="Choose the Psychology_socioty book to put it in your Library",font=("Arial",28,"bold"),fg="#b8860b" , bg="#d8d9ff")
    l.pack(pady=50)
    bpack=Button(rootPsychology_socioty,text="pack",command=rootPsychology_socioty.destroy ,font=("Arial",28,"bold"),fg="#b8860b" , bg="#1e213f",width=10,height=1)
    bpack.place(x=0,y=700)   
    name=StringVar()
    Release_date=StringVar()
    Autor=StringVar()                       
    Publishing_house=StringVar()
    number_of_pages=StringVar()
    
#__________________________list_frame______________________
    list_frame=Frame(rootPsychology_socioty,bg="gray")
    list_frame.place(x=1,y=1,width=360,height=600)
    l=Label(list_frame,text="info about the book",font=("calibri",10,"bold"),fg="black" , bg="red")
    l.place(x=10,y=1)

    lname=Label(list_frame,bg="gray",text="name",font=("calibri",10,"bold"),fg="black" )
    lname.place(x=10,y=50)
    bname=Entry(list_frame,font=("calibri",16),textvariable=name,width=20 ) 
    bname.place(x=120,y=50)

    lRelease_date=Label(list_frame,bg="gray",text="Release_date",font=("calibri",10,"bold"),fg="black" )
    lRelease_date.place(x=10,y=90)
    bRelease_date=Entry(list_frame,font=("calibri",16),textvariable=Release_date,width=20 )
    bRelease_date.place(x=120,y=90)

    lAutor=Label(list_frame,bg="gray",text="Autor",font=("calibri",10,"bold"),fg="black" )
    lAutor.place(x=10,y=130)
    bAutor=Entry(list_frame,font=("calibri",16),textvariable=Autor,width=20 )
    bAutor.place(x=120,y=130)

    lPublishing_house=Label(list_frame,bg="gray",text="Publishing_house",font=("calibri",10,"bold"),fg="black" )
    lPublishing_house.place(x=10,y=170)
    bPublishing_house=Entry(list_frame,font=("calibri",16),textvariable=Publishing_house,width=20 )
    bPublishing_house.place(x=120,y=170)

    lnumber_of_pages=Label(list_frame,bg="gray",text="number_of_pages",font=("calibri",10,"bold"),fg="black" )
    lnumber_of_pages.place(x=10,y=210)
    bnumber_of_pages=Entry(list_frame,font=("calibri",16),textvariable=number_of_pages,width=20 )
    bnumber_of_pages.place(x=120,y=210)

    ldiscraption=Label(list_frame,bg="gray",text="discraption",font=("calibri",10,"bold"),fg="black" )
    ldiscraption.place(x=10,y=250)
    tdiscraption=Text(list_frame,font=("calibri",16),width=30,height=2)
    tdiscraption.place(x=120,y=250)

#_________________________define__________________________

    def getdata(event):
      selected_row=tv.focus()
      data=tv.item(selected_row)
      global row
      row=data["values"]
      name.set(row[1])
      Release_date.set(row[2])
      Autor.set(row[3])
      Publishing_house.set(row[4])
      number_of_pages.set(row[5])
      tdiscraption.delete(1.0,END)
      tdiscraption.insert(END,row[6])

    def displayall():
       tv.delete(*tv.get_children())    
       for row in db_Psychology_socioty.fetch():
        tv.insert("",END,values=row)
    def clear():
       name.set("") 
       Release_date.set("") 
       Autor.set("") 
       Publishing_house.set("") 
       number_of_pages.set("")
       tdiscraption.delete(1.0,END)       

    def delete():
       db_Psychology_socioty.remove(row[0])
       clear()
       displayall()

    def update_book():
        if name.get()=="" or Release_date.get() =="" or Autor.get()=="" or Publishing_house.get()=="" or number_of_pages.get=="" or tdiscraption.get(1.0,END).strip()=="":
            messagebox.showinfo("error","please fill all the entery")
            return
        db_Psychology_socioty.update(
              bname.get(),
              bRelease_date.get(),
              bAutor.get(),
              bPublishing_house.get(),
              number_of_pages.get(),
              tdiscraption.get(1.0,END).strip(),
              row[0])
        messagebox.showinfo("success"," update one book")   
        clear()
        displayall()
              

    def add_book_to_db():
        if bname.get()=="" or bRelease_date.get() =="" or bAutor.get()=="" or bPublishing_house.get()=="" or tdiscraption.get(1.0,END).strip()=="":
            messagebox.showinfo("error","please fill all the entery")
            return
        db_Psychology_socioty.insert(
              bname.get(),
              bRelease_date.get(),
              bAutor.get(),
              bPublishing_house.get(),
              bnumber_of_pages.get(),
              tdiscraption.get(1.0,END).strip())
           
        messagebox.showinfo("success","add new book")   
        clear()
        displayall()

    def add_to_library(book):
      status, msg = add_book(
        book["name"],
        book["release_date"],
        book["author"],
        book["publishing_house"],
        book["number_of_pages"],
        book["description"]
                             )

      if status == "success":
        messagebox.showinfo("Success", msg)
      else:
        messagebox.showerror("Error", msg)    
#________________________bottuns frame_________________________________

    btnframe=Frame(list_frame,bg="white")
    btnframe.place(x=10,y=400,width=335,height=220 )
    badd=Button(btnframe,
            text="Add Details",
            width=14,
            height=1,
            font=("calibri",16),
            fg="white",
            bg="#2c3e50",
            bd=0,
            cursor='hand2',
            command=add_book_to_db
            ).place(x=4, y=5)
    beddit=Button(btnframe,
            text="Edit Details",
            width=14,
            height=1,
            font=("calibri",16),
            fg="white",
            bg="blue",
            bd=0,
            cursor='hand2',
            command=update_book
            ).place(x=4, y=50)
    bdelete=Button(btnframe,
            text="Delete Details",
            width=14,
            height=1,
            font=("calibri",16),
            fg="black",
            bg="red",
            bd=0,
            cursor='hand2',
            command=delete
            ).place(x=170, y=5)
    bclear=Button(btnframe,
            text="clear Details",
            width=14,
            height=1,
            font=("calibri",16),
            fg="red",
            bg="yellow",
            bd=0,
            cursor='hand2',command=clear
            ).place(x=170, y=50)
    
    badd_to_mylibray = Button(
    btnframe,
    text="add to your library",
    width=28,
    height=1,
    font=("calibri", 16),
    fg="black",
    bg="green",
    bd=0,
    cursor='hand2',
    command=lambda: add_to_library({
        "name": bname.get(),
        "release_date": bRelease_date.get(),
        "author": bAutor.get(),
        "publishing_house": bPublishing_house.get(),
        "number_of_pages": bnumber_of_pages.get(),
        "description": tdiscraption.get(1.0, END).strip()
    })).place(x=4, y=95)


#____________________table frame_______________________________________

    tree_frame=Frame(rootPsychology_socioty,bg="white")
    tree_frame.place(x=365,width=940,height=600)
    style=ttk.Style()
    style.configure("mystyle.Treeview",font=("calibri",13),rowheight=50)
    style.configure("mystyle.Treeview.Heading",font=("calibri",13))

    tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7),style="mystyle.Treeview")

    tv.heading("1",text="ID")
    tv.column("1",width="40")
    tv.heading("2",text="name")
    tv.column("2",width="140")
    tv.heading("3",text="Release_date")
    tv.column("3",width="50")
    tv.heading("4",text="Autor")
    tv.column("4",width="120")
    tv.heading("5",text="Publishing_house")
    tv.column("5",width="150")
    tv.heading("6",text="number_of_pages")
    tv.column("6",width="90")
    tv.heading("7",text="discraption")
    tv.column("7",width="150")
    tv['show']='headings'
    tv.bind("<ButtonRelease-1>",getdata)
    tv.pack()
    displayall()
  


