class Employee:
    empcount=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount +=1
    
    def Displaycount(self):
        print "Total employee is ",employee.empcount
    
    def Displayemployee(self):
        print "Name of employee is ",self.name," and salary is ",self.salary
e=Employee("zara",100)
e1=employee("mara",200)
e2=employee("lara",300)
e.Displayemployee()
e.Displaycount()
#inbuit function for object attribute-------------
'''hasattr(e1,"zara")
getattr(e1,"zara")
setattr(e1,name,"sss")
delattr(e1,name)'''
#object is mutable---------------
e.salary=200
e.displayemployee()

