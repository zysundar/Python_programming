from collections import Counter
n=int(input())
l=['cakewalk','simple','easy','easy-medium','medium','medium-hard','hard']
l1=[]
l2=[]
k=' '
while(n>0):
    m= int(input())
    for i in range(0,m):
        l1.append(input())
    #for i in l1:
        #if i not in l:
            #l2.append("No")
#print(l1)            
    d=Counter(l1)
    s1=set(l1)
    for i in s1:
        if d[i]>1:
            p=1
            break;
        else:
            p=0
    
    if(p==0):
        l2.append("yes")
    else:
        l2.append("No")
    l1=[]
    n=n-1
for i in range(0,len(l2)):
    print(l2[i])
