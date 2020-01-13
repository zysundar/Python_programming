fname=raw_input("enter the file name")
c=[1,2,3]
a=10
b={1,2}
try:
    f=open(fname,"r")
    t=f.read()
    print t
    print c[4]
    d=a/0
    d=a/"b"
    print b() 
except IOError:
    print "there is no such type file",fname
except ZeroDivisionError:
    print "don't divide by error"
except IndexError:
    print"out of range"
except TypeError:
    print"divide same type"
except KeyError:
    print"key is not present in dictionary"



############raising error#########
def input_number():
    x=input("enter the number")
    if(x==5):
        raise ValueError,"5 number you can't use"
        print"raise function is working"
input_number()

