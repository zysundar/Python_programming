from Tkinter import *
import Tkinter
t=Tkinter.Tk()
c=Tkinter.Canvas(t,bg="blue",height=450,width=400)
c.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file='att.gif')
c.create_image(50,10,image=gif1,anchor=NW)
t.mainloop()
