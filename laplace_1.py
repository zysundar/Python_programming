import tkMessageBox
import Tkinter
t=Tkinter.Tk()
def login_btn_click():
    #print("Clicked")
    
    entry_1="sundar"
    entry_2="picha"
    username = entry_1
    #entry_1.pack()
    password = entry_2
    #entry_2.pack()
    #print(username, password)
    if username == "sundar" and password == "pichai":
        tkMessageBox.showinfo("Login info", "Welcome sundar")
    else:
        tkMessageBox.showerror("Login error", "Incorrect username")
b=Tkinter.Button(t,text="login",command=login_btn_click)
b.pack()
t.mainloop()
