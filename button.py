import Tkinter
import tkMessageBox
t=Tkinter.Tk()

def f1():
    
    tkMessageBox.showinfo("sss")
b=Tkinter.Button(t,text="press",command=f1)
b.pack()
t.mainloop()
