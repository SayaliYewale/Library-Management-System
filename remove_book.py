from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(rfavicon path)
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove Book")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
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
