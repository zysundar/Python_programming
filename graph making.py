class node:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def __str__(self):
        return self.name+'n'
class edge(node):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getsource(self):
        return self.src
    def getdestination(self):
        return self.dest
    def __str__(self):
        return self.src.getname()+'->'+self.dest.getname()+'/n'
a=node("phagwara")
b=node("jalandhar")
c=node("ludhiana")
print a,b,c
e=edge(a,b)
e1=edge(a,c)
e2=edge(b,c)
print e,e1,e2
