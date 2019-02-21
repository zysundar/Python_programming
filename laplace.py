
import Tkinter as tk
from Tkinter import*
from tkMessageBox import*
t=tk.Tk()
def login_btn_click():
    #print("Clicked")
    entry_1="sundar"
    entry_2="pichai"
    username = entry_1
    #entry_1.pack()
    password = entry_2
    #entry_2.pack()
    #print(username, password)
    if username == "sundar" and password == "pichai":
        tkMessageBox.showinfo("Login info", "Welcome John")
    else:
        tkMessageBox.showerror("Login error", "Incorrect username")
def login_page():
    #l1=tk.Label(f2,text="User Name")
    #l1.pack(side=TOP)
    #t=tk.Tk()
    label_1 = Label(t, text="Username")
    label_1.pack()
    entry_1 = Entry(t)
    entry_1.pack()
    label_2 = Label(t, text="Password")
    label_2.pack()   
    entry_2 = Entry(t, show="*")
    entry_2.pack()
    '''self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)'''
    checkbox = Checkbutton(t, text="Keep me logged in")
    checkbox.pack()
    logbtn = Button(t, text="Login", command =login_btn_click)
    logbtn.pack()
    t.pack()
B1 = tk.Button(t, text="New User",bg="blue")#command=register_page)
B1.pack()
B2 = tk.Button(t, text="Login",bg="Red",command=login_page)
B2.pack()
B3 = tk.Button(t, text="Available parking",bg="blue")#command=register_page)
B3.pack()


t.mainloop()
