import Tkinter as tk
from Tkinter import*

def login_page():
    f2.pack_forget()
    f5.pack_forget()
    f3.pack()
    f4.pack()
    f1.pack()
def register_page():
    f1.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f2.pack()
    f5.pack()
def available_parking():
    f6.pack()
master = tk.Tk()

# ________________________________________Login page___________________________________________
f1 = tk.Frame(master)
l1 = tk.Label(f1, text="pass Word")
l1.pack(side=LEFT)
E1=Entry(f1,bd=5)
E1.pack(side=LEFT)
f4=tk.Frame(master)
l = tk.Label(f4, text="User Name")
l.pack(side=LEFT)
a1=Entry(f4,bd=5)
a1.pack(side=RIGHT)
def login_btn_click():
    #print("Clicked")
    username = a1.get()
    #entry_1.pack()
    password = E1.get()
    #entry_2.pack()
    #print(username, password)
    if username == "sundar" and password == "pichai":
        
        tm.showinfo("Login info", "Welcome John")
    else:
        tm.showerror("Login error", "Incorrect username")

f3=tk.Frame(master)
B1 = tk.Button(f3, text="New User",bg="blue", command=register_page)
b2=tk.Button(f3,text="Login Now",bg="blue",command=login_btn_click)
b2.pack(side=LEFT)
B1.pack()
B4 = tk.Button(f3, text="Available Parking",bg="blue", command=available_parking)
B4.pack()
f3.pack(side=BOTTOM)
f4.pack(side=TOP)
# ___________________________________________Register page_____________________________________
f2 = tk.Frame(master)
l8=tk.Label(f2,text="User Name")
l8.pack(side=TOP)
b8=tk.Entry(f2,bd=5)
b8.pack(side=TOP)
l2 = tk.Label(f2, text="Reg.No.")
l3=tk.Entry(f2,bd=5)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
b3=tk.Label(f2,text="Hostel/Block")
b3.pack(side=LEFT)
l4=tk.Entry(f2,bd=5)
l4.pack(side=LEFT)
var = IntVar()
f5=tk.Frame(master)
b4=tk.Label(f5,text="Gender")
b4.pack(side=LEFT)
R1 = Radiobutton(f5, text="Male", variable=var, value=1)
R1.pack( anchor = W ,side=LEFT)
R2 = Radiobutton(f5, text="Female", variable=var, value=2)
R2.pack( anchor = W,side=LEFT )
b5=tk.Label(f5,text="Mobile no")
b5.pack(side=LEFT)
l5=Entry(f5,bd=5)
l5.pack(side=LEFT)
b6=tk.Label(f5,text="Email Id")
b6.pack(side=LEFT)
l6=tk.Entry(f5,bd=5)
l6.pack()
b2 = tk.Button(f2, text="Return Login Page", command=login_page)
b2.pack(anchor= S)
f5.pack(side=BOTTOM)
B2=tk.Button(f5,text="Submit",bg="blue")
B2.pack(side=RIGHT)
# _____________________________________________________Availability checking______________________________________________
f6=Frame(master)
l7=tk.Label(f6,text="reg.NO")
l7.pack()
b7=tk.Entry(f6,bd=5)
b7.pack()
l8=tk.Label(f6,text="Parking Block")
l8.pack()
#b8=tk.Entry(f6,bd=5)
#b8.pack()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(f6, text = "34", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
C2 = Checkbutton(f6, text = "29", variable = CheckVar2,onvalue = 1, offvalue = 0, height=0,width = 0)
C1.pack()
C2.pack()
l9=tk.Label(f6,text="Price")
l9.pack()
b9=tk.Entry(f6,bd=5,text="in rs")
b9.pack()
B5=tk.Button(f6, text="Order",bg="blue")
B5.pack()
# show first frame
f1.pack()
#f2.pack()
master.mainloop()
