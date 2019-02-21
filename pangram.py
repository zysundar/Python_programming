a=[]
sum1=0
value=list(map(int,input().split()))
s="abcdefghijklmnopqrstuvwxyz"
keys=list(s)
d=dict(zip(keys,value))
#print(d)
s1=""
s1=list(input())
for i in keys:
    if i in s1:
        pass
    else:
        a.append(keys[i])
for i in a:
    sum1=sum1+d[i]
print(sum1)
