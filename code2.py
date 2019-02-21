k=int(input())
l=[]
while(k>0):
    n=int(input())
    a=[]
    a[0:n+1]=list(map(int,input().split()))
    b=[]
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if i==j:
                pass
            else:    
                b.append("%d%d" % (a[i],a[j]))
    l.append(2*len(b))
    a=[]
    b=[]
    k=k-1
for i in range(0,len(l)):
    print(l[i])
