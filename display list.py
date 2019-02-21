class song:
    def __init__(self,lis):
        self.lis=lis
    def display(self):
        for i in self.lis:
            
            print "list =",i

l=(["my name is","my name is","i am from"])

    
e=song(l)
e.display()
'print(e.display())'      
