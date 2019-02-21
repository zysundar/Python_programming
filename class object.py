class employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount +=1
    def displaycount(self):
        print "total employee=",employee.empcount
    def displayemployee(self):
        print "name of employee=",self.name,"salary =",self.salary
e=employee("zara",100)
e1=employee("mara",200)
e2=employee("lara",300)
e.displayemployee()
e.displaycount()
#inbuit function for object attribute-------------
'''hasattr(e1,"zara")
getattr(e1,"zara")
setattr(e1,name,"sss")
delattr(e1,name)'''
#object is mutable---------------
e.salary=200
e.displayemployee()

