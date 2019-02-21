import marshal
f=open("hostel.txt","w")
#f.write("sundaram")
marshal.dump([1,2,3,4,5],f)
f.close()
#import pickle
f=open("hostel.txt","r")
t=marshal.load(f)
print t,type(t)
f.close()
