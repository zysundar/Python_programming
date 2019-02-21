x=raw_input("enter the number")
z=raw_input("enter the string")
try:
    print(z/0)
    print(int(z))
    y=int(x)
    print "number is interger type",pow(y,2)
except (ValueError,TypeError,ZeroDivisionError):
    #print "number is string  so can't find square"
    #print "typeerror"
     print "zerodivisionerror"
     assert "sssss"
