import Tkinter
from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style

class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        self.initUI()

    def initUI(self):
        
        self.parent.title("AUTO TIPS")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Status")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="Drive Command", command=win3)
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Tester Manual Control", command=win2)
        cbtn.grid(row=2, column=3, pady=4)

        dbtn = Button(self, text="Auto Run", command=AutoTIPS)
        dbtn.grid(row=3, column=3, pady=4)

        obtn = Button(self, text="OK", command=self.parent.destroy)
        obtn.grid(row=5, column=3)

####################################################################################################################################################        
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

failure_max = 3
passwords = [('Aung', 'Aung')]

def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

def enter(event):
    check_password()

def check_password(failures=[]):
    # Collect 1's for every failure and quit program in case of failure_max failures 
    print(user.get(), password.get())
    if (user.get(), password.get()) in passwords:
        root.destroy()
        print('Logged in')
        return
    failures.append(1)
    if sum(failures) >= failure_max:
        root.destroy()
        raise SystemExit('Unauthorized login attempt')
    else:
        root.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))


root = tk.Tk()
root.geometry('300x160')
root.title('Enter your information')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "User name:", 16, show='')
password = make_entry(parent, "Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=check_password)
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)

user.focus_set()

parent.mainloop()        

####################################################################################################################################################              

def win2():

    board = Tkinter.Toplevel()
    board.title("Tester Manual Control")
    s1Var = Tkinter.StringVar()
    s2Var = Tkinter.StringVar()
    s3Var = Tkinter.StringVar()
    s4Var = Tkinter.StringVar()
    s5Var = Tkinter.StringVar()
    s6Var = Tkinter.StringVar()
    s7Var = Tkinter.StringVar()
    s8Var = Tkinter.StringVar()

    s1Var.set(" Tester 1")
    s2Var.set(" Tester 2")
    s3Var.set(" Tester 3")
    s4Var.set(" Tester 4")
    s5Var.set(" Tester 5")
    s6Var.set(" Tester 6")
    s7Var.set(" Tester 7")
    s8Var.set(" Tester 8")

    square1Label = Tkinter.Label(board,textvariable=s1Var)
    square1Label.grid(row=1, column=500)
    square2Label = Tkinter.Label(board,textvariable=s2Var)
    square2Label.grid(row=2, column=500)
    square3Label = Tkinter.Label(board,textvariable=s3Var)
    square3Label.grid(row=3, column=500)
    square4Label = Tkinter.Label(board,textvariable=s4Var)
    square4Label.grid(row=4, column=500)
    square5Label = Tkinter.Label(board,textvariable=s5Var)
    square5Label.grid(row=5, column=500)
    square6Label = Tkinter.Label(board,textvariable=s6Var)
    square6Label.grid(row=6, column=500)
    square7Label = Tkinter.Label(board,textvariable=s7Var)
    square7Label.grid(row=7, column=500)
    square8Label = Tkinter.Label(board,textvariable=s8Var)
    square8Label.grid(row=8, column=500)



####################################################################################################################################################

def win3():

    board = Tkinter.Toplevel()
    board.title("Drive Command")
    codeloadButton = Tkinter.Button(board, text="Code Load", command=win4)
    codeloadButton.grid(row=100, column=50)
    clearButton = Tkinter.Button(board, text="Clear Dos Table", command=win5)
    clearButton.grid(row=500, column=50)

####################################################################################################################################################

def win4():

    board = Tkinter.Toplevel()
    board.title("Code Load")

####################################################################################################################################################

def win5():

    board = Tkinter.Toplevel()
    board.title("Clear Dos Table")

####################################################################################################################################################

def main():
  root = Tk()
  root.geometry("350x300+300+300")
  app = MainWindow(root)
  root.mainloop()  

if __name__ == '__main__':
    main()
