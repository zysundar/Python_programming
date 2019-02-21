class parent:
    def mymethod(self):
        print ("calling parent parent function")
class child(parent):
    def mymethod(self):
        print ("calling child function")
c=child()
c.mymethod()
d=parent()
d.mymethod()
c=d
c.mymethod()

#__del__
#__repr__
#__cmp__
#__str__
