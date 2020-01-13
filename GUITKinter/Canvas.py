import Tkinter

win=Tkinter.Tk()
can=Tkinter.canvas(win,bg="blue",height=450,width=400)
cord=10,20,40,50
arc=can.create_arc(cord,start=0,extent=120,fill="red")
ct=can.create_line(40,50,100,120)
can.pack()
win.mainloop()
