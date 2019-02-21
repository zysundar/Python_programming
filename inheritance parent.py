class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def getname(self):
        print ("full name=",self.fname+self.lname)
       # print ("lname=",self.lname)
class employee(person):
    def __init__(self,fname,lname,number):
        person.__init__(self,fname,lname)
        self.number=number
    def display(self):
        print ("employee id is",self.number)
        return(self.getname())
class Boss(person):
    def __init__(self,fname,lname,title):
        
        #self.fname=fname
       # self.lname=lname
        person.__init__(self,fname,lname)
        self.title=title
    def display_1(self):
       # print "full name=",fname,lname
        print ("title of Boss=",self.title)
        return("full name =",self.getname())
person_1=person("math","hoang")
employee_1=employee("math","hoang","1234")
employee_2=employee("blog","spot","4321")
boss_1=Boss("mathhoang","blogspaot","ceo")
person_1.getname()
employee_1.display()
boss_1.display_1()
#____issubclass(sub,sup)____
issubclass(Boss,person)
#-----isinstance(obj,class)--------
isinstance(person_1,person)
'''c=Boss("Hr")
c.display_1()
d=employee(111)
d.display()
e=person("sss","rrrr")
e.getname()
'''
