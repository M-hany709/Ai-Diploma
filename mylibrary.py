from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db_mylibrary import librarym

db_mylibrary=librarym("books.db")

def add_book(name, release_date, author, publishing_house, number_of_pages, description):
    if not all([name, release_date, author, publishing_house, description.strip()]):
        return "error", "Please fill all the fields."

    db_mylibrary.insert(name, release_date, author, publishing_house, number_of_pages, description)
    return "success", "Book added successfully."

def open_root_mylibrary():
    rootmylibrary=Toplevel()
    rootmylibrary.attributes("-fullscreen", True)
    rootmylibrary.title("Library system mangement") 
    rootmylibrary.resizable(False,False)
    rootmylibrary.configure(bg="gray")
    l=Label(rootmylibrary,text="   Choose the book to put it in your Library",font=("Arial",28,"bold"),fg="#b8860b" , bg="#d8d9ff")
    l.pack(pady=50)
    bpack=Button(rootmylibrary,text="pack",command=rootmylibrary.destroy ,font=("Arial",28,"bold"),fg="#b8860b" , bg="#1e213f",width=10,height=1)
    bpack.place(x=0,y=700)

    name=StringVar()
    Release_date=StringVar()
    Autor=StringVar()                       
    Publishing_house=StringVar()
    number_of_pages=StringVar()
    
#__________________________list_frame______________________
    list_frame=Frame(rootmylibrary,bg="gray")
    list_frame.place(x=1,y=1,width=360,height=600)
    l=Label(list_frame,text="info about the book",font=("calibri",10,"bold"),fg="white" , bg="#1e213f")
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
       for row in db_mylibrary.fetch():
        tv.insert("",END,values=row)
    def clear():
       name.set("") 
       Release_date.set("") 
       Autor.set("") 
       Publishing_house.set("") 
       number_of_pages.set("")
       tdiscraption.delete(1.0,END)       

    def delete():
       db_mylibrary.remove(row[0])
       clear()
       displayall()

    def add_book_to_mylibrary():
      name_val = bname.get()
      release_date_val = bRelease_date.get()
      author_val = bAutor.get()
      publishing_house_val = bPublishing_house.get()
      number_of_pages_val = number_of_pages.get()
      description_val = tdiscraption.get(1.0, END)

      status, message = add_book(name_val, release_date_val, author_val, publishing_house_val, number_of_pages_val, description_val)
      messagebox.showinfo(status, message)
    
      if status == "success":
        clear()
        displayall()
    
    
#________________________bottuns frame_________________________________

    btnframe=Frame(list_frame,bg="gray")
    btnframe.place(x=10,y=400,width=335,height=100 )
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
            ).place(x=4, y=5)
    bclear=Button(btnframe,
            text="clear Details",
            width=14,
            height=1,
            font=("calibri",16),
            fg="black",
            bg="green",
            bd=0,
            cursor='hand2',command=clear
            ).place(x=170, y=5)

#____________________table frame_______________________________________

    tree_frame=Frame(rootmylibrary,bg="white")
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
  

