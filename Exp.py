#******LOGIN PAGE******
from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
import sysexecute
from mysql.connector import Error
py=sysexecute


#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")


#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

        def check():


                    self.label = Label(self, text="LOGIN", bg = 'gray' , fg = 'black', font=("courier-new", 24,'bold'))
                    self.label.place(x=550, y=90)
                    self.label1 = Label(self, text="User-Id" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label1.place(x=370, y=180)
                    self.user_text = Entry(self, textvariable=self.a, width=45)
                    self.user_text.place(x=480, y=190)
                    self.label2 = Label(self, text="Password" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label2.place(x=340, y=250)
                    self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
                    self.pass_text.place(x=480, y=255)
                    self.butt = Button(self, text="Login",bg ='white', font=10, width=8, command=chex).place(x=580, y=300)
                    self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
                    self.label3.place(x=350, y=30)


        check()

Lib().mainloop()


#*****SEARCH BOOK*****
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500, bg='gray')
        self.canvas.pack()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        l1=Label(self,text="Search Library",bg='gray', font=("Courier new",20,'bold')).place(x=290,y=20)
        l = Label(self, text="Search By",bg='gray', font=("Courier new", 15, 'bold')).place(x=60, y=96)
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where name LIKE %s",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where author LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Author Name not found")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where book_id LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
        b=Button(self,text="Find",width=15,bg='gray',font=("Courier new",10,'bold'),command=ge).place(x=460,y=148)
        c=ttk.Combobox(self,textvariable=g,values=["Book Name","Author Name","Book Id"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Enter",bg='gray', font=("Courier new", 15, 'bold')).place(x=100, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Book Author')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Search().mainloop()


#******ISSUE BOOK*****
from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys

py = sys.executable


# creating window
class issue(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.title('Library Admisintration')
        self.maxsize(440, 300)

        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        c = StringVar()
        d = StringVar()

        # verifying input
        def isb():
            if (len(c.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            elif (len(d.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select availability from book where availability = 'YES' and book_id = %s",
                                          [c.get()])
                    self.pc = self.mycursor.fetchall()
                    try:
                        if self.pc:
                            print("success")
                            book = c.get()
                            stud = d.get()
                            now = datetime.now()
                            idate = now.strftime('%Y-%m-%d %H:%M:%S')
                            self.mycursor.execute(
                                "Insert into issue_book(book_id,stud_id,issue_date,return_date) values (%s,%s,%s,%s)",
                                [book, stud, idate, ''])
                            self.conn.commit()
                            self.mycursor.execute("Update book set availability = 'NO' where book_id = %s", [book])
                            self.conn.commit()
                            messagebox.showinfo("Success", "Successfully Issue!")
                            ask = messagebox.askyesno("Confirm", "Do you want to add another?")
                            if ask:
                                self.destroy()
                                os.system('%s %s' % (py, 'issueTable.py'))
                            else:
                                self.destroy()
                        else:
                            messagebox.showinfo("Oop's", "Book id " + c.get() + " is not available")
                    except Error:
                        messagebox.showerror("Error", "Check The Details")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")

        # label and input box
        Label(self, text='Book Issuing', bg='gray', font=('Courier new', 24)).place(x=135, y=40)
        Label(self, text='Book ID:', bg='gray', font=('Courier new', 15), fg='black').place(x=55, y=100)
        Entry(self, textvariable=c, width=40).place(x=160, y=106)
        Label(self, text='Student ID:', bg='gray', font=('Courier new', 15), fg='black').place(x=20, y=150)
        Entry(self, textvariable=d, width=40).place(x=160, y=158)
        Button(self, text="ISSUE", width=20, command=isb).place(x=200, y=200)


issue().mainloop()


#*****RETURN BOOK*****
from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
py = sys.executable


class ret(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.title("Return")
        self.maxsize(420,280)
        self.canvas = Canvas(width=500, height=417, bg='gray')
        l1 = Label(self, text="Return Book", bg='gray', font=("Courier new", 20, 'bold')).place(x=100, y=20)
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s", [idate,a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")
        Label(self, text='Return Book', fg='red',font=('arial', 35, 'bold')).pack()
        Label(self, text='Enter Book ID', font=('Comic Scan Ms', 15, 'bold')).place(x=20, y=120)
        Entry(self, textvariable=a, width=40).place(x=165, y=124)
        Button(self, text="Return", width=25, command=qui).place(x=180, y=180)
ret().mainloop()


#*****SEARCH STUDENT*****
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import os,glob
import mysql.connector
from mysql.connector import Error

class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Student")
        self.maxsize(800,520)
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        l1=Label(self,text="Search Student",bg='gray', font=("Courier new",20,'bold')).place(x=290,y=40)
        l = Label(self, text="Search By",bg='gray', font=("Courier new", 15, 'bold')).place(x=180, y=100)


        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("","end",text = row[0], values = (row[1],row[2],row[3]))


        def ge():
            if (len(self.entry.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(self.combo.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+self.combo.get())
            elif self.combo.get() == 'Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    name = self.entry.get()
                    self.mycursor.execute("Select * from student where name like %s",['%'+name+'%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's","Name not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif self.combo.get() == 'ID':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.mycursor = self.conn.cursor()
                    id = self.entry.get()
                    self.mycursor.execute("Select * from student where stud_id like %s", ['%' + id + '%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Id not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")


        self.b= Button(self,text="Find",width=8,font=("Courier new",8,'bold'),command= ge )
        self.b.place(x=400,y=170)
        self.combo=ttk.Combobox(self,textvariable=g,values=["Name","ID"],width=40,state="readonly")
        self.combo.place(x = 310, y = 105)
        self.entry = Entry(self,textvariable=f,width=43)
        self.entry.place(x=310,y=145)
        self.la = Label(self, text="Enter",bg = 'gray', font=("Courier new", 15, 'bold')).place(x=180, y=140)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Student Name', 'Phone Number', 'Address'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Student ID', anchor='w')
        self.listTree.column("#0", width=100, anchor='w')
        self.listTree.heading("Student Name", text='Student Name')
        self.listTree.column("Student Name", width=200, anchor='center')
        self.listTree.heading("Phone Number", text='Phone Number')
        self.listTree.column("Phone Number", width=200, anchor='center')
        self.listTree.heading("Address", text='Address')
        self.listTree.column("Address", width=200, anchor='center')
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=743,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Search().mainloop()


#*****REMOVE USER*****
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove User")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        l1 = Label(self, text="Remove Student", bg='gray', font=("Courier new", 20, 'bold')).place(x=100, y=10)
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")
        Label(self, text = "Enter User Id: ",bg='gray',fg='black',font=('Courier new', 15, 'bold')).place(x = 5,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self, text='Remove', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()


#*****REMOVE BOOK*****
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove Book")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        l1 = Label(self, text="Remove Book", bg='gray', font=("Courier new", 20, 'bold')).place(x=100, y=10)
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Name")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the book?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                                            database='library',
                                                            user='root',
                                                            password='')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from book where name = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","Book Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")
        Label(self, text = "Enter Book Name: ",bg='gray',fg='black',font=('Courier new', 12, 'bold')).place(x = 3,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self, text='Remove', width=15, font=('arial', 10),command = ent).place(x=210, y = 90)



Rem().mainloop()


#*****ADD BOOK*****
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book')
        self.canvas = Canvas(width=500, height=500, bg='gray')
        l1 = Label(self, text="Add Book", bg='gray', font=("Courier new", 20, 'bold')).place(x=100, y=20)
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        #verifying Input
        def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,author,availability) values (%s,%s,%s)",[b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")
        #creating input box and label
        Label(self, text='').pack()
        Label(self, text='Book Details:',bg='gray',fg='black',font=('Courier new', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Book Name:',bg='gray',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=b, width=30).place(x=170, y=182)
        Label(self, text='Book Author:',bg='gray',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=c, width=30).place(x=170, y=232)
        Button(self, text="Submit", command=b_q).place(x=245, y=300)
Add().mainloop()


#*****ADD USER*****
from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",[u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Add_Student.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
#label and input
        Label(self, text='User Details', bg='gray', fg='black', font=('Courier new', 25, 'bold')).place(x=130, y=22)
        Label(self, text='Username:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='Password:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Button(self, text="Submit", width=15, command=insert).place(x=230, y=220)
reg().mainloop()


#*****MAIN MODULE*****

from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk

import mysql.connector
from mysql.connector import Error

py=sys.executable

#creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        self.configure(bg='gray')
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEMS')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
#calling scripts
        def a_s():
            os.system('%s %s' % (py, 'Add_Student.py'))

        def a_b():
            os.system('%s %s' % (py, 'Add_Books.py'))

        def r_b():
            os.system('%s %s' % (py, 'remove_book.py'))

        def r_s():
            os.system('%s %s' % (py, 'Remove_student.py'))

        def ib():
            os.system('%s %s' % (py, 'issueTable.py'))

        def ret():
            os.system('%s %s' % (py, 'ret.py'))

        def sea():
            os.system('%s %s' % (py,'Search.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to Logout?")
            if conf:
             self.destroy()
             os.system('%s %s' % (py, 'Main.py'))



      # def handle(event):
        #     if self.listTree.identify_region(event.x,event.y) == "separator":
        #         return "break"
        def add_user():
            os.system('%s %s' % (py, 'Reg.py'))
        def rem_user():
            os.system('%s %s' % (py, 'Rem.py'))
        def sest():
            os.system('%s %s' % (py,'Search_Student.py'))

#creating table

        self.listTree = ttk.Treeview(self,height=14,columns=('Student','Book','Issue Date','Return Date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='ID')
        self.listTree.column("#0", width=50,minwidth=50,anchor='center')
        self.listTree.heading("Student", text='Student')
        self.listTree.column("Student", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Book", text='Book')
        self.listTree.column("Book", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=125, minwidth=125, anchor='center')
        self.listTree.place(x=320,y=360)
        self.vsb.place(x=1028,y=361,height=287)
        self.hsb.place(x=320,y=650,width=700)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))

        list1 = Menu(self)
        list1.add_command(label="Student", command=a_s)
        list1.add_command(label="Book", command=a_b)

        list3 = Menu(self)
        list3.add_command(label = "Add User",command = add_user)
        list3.add_command(label = "Remove User",command = rem_user)


        self.mymenu.add_cascade(label='Add', menu=list1)
        self.mymenu.add_cascade(label = 'Admin Tools', menu = list3)

        self.config(menu=self.mymenu)

        def ser():
            if(len(self.studid.get())==0):
                messagebox.showinfo("Error", "Empty Field!")
            else:

             try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                cursor = conn.cursor()
                change = int(self.studid.get())
                cursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id and s.stud_id = %s",[change])
                pc = cursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
             except Error:
                #print(Error)
              messagebox.showerror("Error","Something Goes Wrong")
        def ent():
            if (len(self.bookid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:
             try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                book = int(self.bookid.get())
                self.myCursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id and b.book_id = %s",[book])
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in self.pc:
                        self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued")
             except Error:
                messagebox.showerror("Error", "Something Goes Wrong")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='')
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm","Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Reg.py'))
                else:
                    #label and input box
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM',fg='black',bg="gray" ,font=('Courier new', 30, 'bold'))
                    self.label3.place(x=350, y=22)
                    self.label4 = Label(self, text="ENTER STUDENT",bg="gray", font=('Courier new', 18, 'bold'))
                    self.label4.place(x=130, y=107)
                    self.studid = Entry(self, textvariable=self.a, width=90)
                    self.studid.place(x=405, y=110)
                    self.srt = Button(self, text='Search', width=15, font=('arial', 10),command = ser).place(x=1000, y=106)
                    self.label5 = Label(self, text="ENTER THE BOOK ID",bg="gray", font=('Courier new', 18, 'bold'))
                    self.label5.place(x=75, y=150)
                    self.bookid = Entry(self, textvariable=self.b, width=90)
                    self.bookid.place(x=405, y=160)
                    self.brt = Button(self, text='Find', width=15, font=('arial', 10),command = ent).place(x=1000, y=150)
                    self.label6 = Label(self, text="INFORMATION DETAILS",bg="gray",  font=('Courier new', 15, 'underline', 'bold'))
                    self.label6.place(x=560, y=300)
                    self.button = Button(self, text='Search Student', width=25, font=('Courier new', 10), command=sest).place(x=240,y=250)
                    self.button = Button(self, text='Search Book', width=25, font=('Courier new', 10), command=sea).place(x=520,y=250)
                    self.brt = Button(self, text="Issue Book", width=15, font=('Courier new', 10), command=ib).place(x=800, y=250)
                    self.brt = Button(self, text="Return Book", width=15, font=('Courier new', 10), command=ret).place(x=1000, y=250)
                    self.brt = Button(self, text="LOGOUT", width=15,bg="red", font=('Courier new', 10), command=log).place(x=1150, y=105)
            except Error:
                messagebox.showerror("Error", "Something Goes Wrong")
        check()

MainWin().mainloop()
