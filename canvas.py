import Tkinter
import tkMessageBox
t=Tkinter.Tk()
c=Tkinter.canvas(t,bg="blue",height=450,width=400)
cord=10,20,40,50
arc=c.create_arc(cord,start=0,extent=120,fill="red")
ct=c.create_line(40,50,100,120)
c.pack()
t.mainloop()
