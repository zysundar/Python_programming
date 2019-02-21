from Tkinter import *
import Tkinter
import tkMessageBox
t=Tkinter.Tk()
CheckVar1=IntVar()
CheckVar2=Intvar()
c=t.CheckButton(t,text="Music",Variable=CheckVar1,onvalue=1,\
                 offvalue=0,height=5,width=20)
c.Pack()
t.mainloop()
