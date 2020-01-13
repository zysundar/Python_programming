import Tkinter
import tkMessageBox
win = Tkinter.Tk()

def func1():
    tkMessageBox.showinfo("Hello There!!!")

button1=Tkinter.Button(win,text="Click Here!",command=func1)
button.pack()
win.mainloop()
