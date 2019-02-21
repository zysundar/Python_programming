class fruit:
    def __init__(self,name,tast,color,poisnous):
        self.name=name
        self.tast=tast
        self.color=color
        self.poisnous=poisnous
    def display(self):
        if(self.name=='orange'||self.name=='apple'||self.name=='lemon'):
            print "you choosen fruit is ",self.name
            if(self.tast=='sweet'):
            print
