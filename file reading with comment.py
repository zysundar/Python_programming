#f=open("file1.txt","w")
#for i in range(3):
 #   name=raw_input("enter the string")
#    f.write(name+'/n')
#f.close()
f=open("hostel.txt","r")
f1=open("file2.txt","w")
'''for i in f:
    if(i==' '):
        break
    if(i=='#'):
        break
    print i
    f1.write(i)'''
while True:    
    t=f.read()
    '''if(t!=" "):
        continue'''
    u=(f1.write(t))
    print u
f1.close()
        
