class Song:
    
    def __init__(self,lis):
        self.lis=lis
    
    def Display(self):
        for i in self.lis:
            print "list =",i

l=(["my name is","my name is","i am from"])
e=Song(l)
e.display()
#print(e.display())     
