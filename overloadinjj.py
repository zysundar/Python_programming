import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def __str__(self):
        return "circle (%d)"+str(self.radius)
    def set_radius(self,radius):
        self.radius=radius
    def display(self):
        print self.radius
    def area(self):
        return math.pi*self.radius**2
    def __add__(self,other_circle):
        return self.radius+other_circle.radius
    def __lt__(self,other_circle):
        return self.radius<other_circle.radius
    def __gt__(self,other_circle):
        return self.radius>other_circle.radius
    def __mod__(self,other_circle):
        return self.radius/other_circle.radius
    def __ne__(self,other_circle):
        return self.radius!=other_circle.radius
c1=circle(4)
#print(c1.set_radius(3))
c2=circle(2)
c3=c1+c2
print(c3)
print(c1.area())
print(c2.area())
c2.set_radius(5)
c3=c1+c2
print(c3)
c4=c1>c2
c5=c1<c2
print("greater value ",c4)

