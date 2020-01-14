import pickle
f=open("abc.txt","w")
pickle.dump([1,2,3,4,5],f)
f.close()
import pickle
f=open("abc.txt","r")
t=pickle.loads(f)
print t
f.close()
