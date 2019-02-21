f=open("room.txt","r")
f1=open("ho.txt","r")
for l in f:    
    c=f1.readlines(3)
print c
f.close()
f1.close()
