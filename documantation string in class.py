class myclass:
    " my name is sundaram"
    a=10
    def f(self):
        print "hello"
ob=myclass()
ob.f()
# in built class attribute-----------
print(myclass.a)
print(myclass.__doc__)
print(myclass.__name__)
print(myclass.__module__)
print(myclass.__bases__)
print(ob.f())
