from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Search(Tk):
    def __init__(tanmayee):
        super().__init__()
        f = StringVar()
        g = StringVar()
        tanmayee.title("Search Book")
        tanmayee.maxsize(800,500)
        tanmayee.minsize(800,500)
        tanmayee.canvas = Canvas(width=800, height=500, bg='gray')
        tanmayee.canvas.pack()
        tanmayee.iconbitmap(r"C:\Users\yewal\Downloads\favicon.ico")
        l1=Label(text="Search Library",bg='gray', font=("Courier new",20,'bold')).place(x=290,y=20)
        l = Label(tanmayee, text="Search By",bg='gray', font=("Courier new", 15, 'bold')).place(x=60, y=96)
        def insert(data):
            tanmayee.listTree.delete(*tanmayee.listTree.get_children())
            for row in data:
                tanmayee.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))



Search().mainloop()