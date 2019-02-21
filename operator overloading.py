class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "vector (%d,%d)"%(self.a,self.b)
    def __add__(self,other):
        return vector(self.a+other.a,self.b+other.b)

v1=vector(-10,10)
v2=vector(5,-2)
print (v1+v2)
#__truediv__(self,other)    #division
#__lt__(self,other)   #less then
#__le__(self,other)  #less then or equal to
#__eq__(self,other) #equal to
#__ne__(self,other) #not equal to
#__gt__(self,other) #greather then
#__ge__(self,other) #greater or equal to
#__mod__(self,other) #remainde
#__
