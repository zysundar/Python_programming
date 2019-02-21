from Tkinter import *
import pickle
import tkMessageBox
root = Tk()
root=Frame(root)

def login(pas,user):
    file1=open("database.txt",'r')
    b=pickle.load(file1)
    k=[i for i in b.keys()]
    if (user in k):
        if(pas==b[user]):
            tkMessageBox.showinfo("Login" ,"succesful login")
        else:
            tkMessageBox.showerror("login", "Wrong Password")
    else:
        tkMessageBox.showwarning("Login" ,"Username not found")  
    


label_1 = Label(root, text="Username")
label_2 = Label(root, text="Password")
v=StringVar()
entry_1 = Entry(root)
v=entry_1.get()
v1=StringVar()
entry_2 = Entry(root)
v1=entry_2.get()
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checkbox = Checkbutton(root, text="Keep me logged in",command=login(v,v1))
checkbox.grid(columnspan=2)
root.pack()
root.mainloop()
