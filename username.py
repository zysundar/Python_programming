from Tkinter import *
root = Tk()
root=Frame(root)

label_1 = Label(root, text="Username")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(columnspan=2)
username = "john"
input("Username: ")
while not username:
    if username == "john":
        print("Welcome")
    else:
        print("User not found")


password = "password"
while not password:
    input("password: ")
    if password == "password":
        print("Logged in")
    else:
        print("Incorrect password")
root.pack()
root.mainloop()
