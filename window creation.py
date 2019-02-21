import Tkinter
import tkMessageBox
t=Tkinter.Tk()
def A():
    tkMessageBox.showinfo("title","Lovely Profssional University")
    tkMessageBox.askquestion("title","punjab University")
    tkMessageBox.askokcancel("title","Chandigarh UNIversity")
    tkMessageBox.showerror("title","system Memory Low");
    tkMessageBox.showwarning("Don't Use My LAptop")
B=Tkinter.Button(t,text="hello",command=A,height=5,width=5,anchor="center",bg="red",cursor="clock")
B.pack()
t.mainloop()
