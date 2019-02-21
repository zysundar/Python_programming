f=open("room.txt","a")
for line in range(4):
    name=raw_input("enter the name")
    f.write(name+'\n')
f.close()
f=open("room.txt","r")
for l in f:
    print l[:-1]
f.close()
f=open("room.txt","r")
t=f.read()
print(t)
print (type(t))
