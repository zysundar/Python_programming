class Parent:
    parentattr=100
    
    def __init__(self):
        print "Calling Parent Constructer "
        
    def Parentattr(self,attr):
        Parent.attr = attr
    
    def Parentmethod(self):
        print "Calling Parent Method "
    
    def Getattrr(self):
        print "Get Attr= ",parent.attr
        
class Child(Parent):
    
    def __init__(self):
        print"Calling Child Constucter"
    
    def Childhood(self):
        print "Calling Childhood Method"
c=Child()
c.Childhood()
c.Parentmethod()
c.Parentattr(200)

c.Getattr()
