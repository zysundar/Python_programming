class parent:
    parentattr=100
    def __init__(self):
        print "calling parent constructer"
    def parentattr(self,attr):
        parent.attr=attr
    def parentmethod(self):
        print "calling parent method"
    def getattrr(self):
        print "get attr=",parent.attr
class child(parent):
    def __init__(self):
        print"calling child constucter"
    def childhood(self):
        print "calling childhood method"
c=child()
c.childhood()
c.parentmethod()
c.parentattr(200)
c.getattr()
c.getattr()
