l=[]
l1=[]
n=int(input())
l = list(map(int, input().split()))
#for i in range(0,n):
 #   k=int(input())
  #  l.append(k)
m1=max(l)
l.remove(m1)
m2=max(l)
l.remove(m2)
#print(l)
l=[m1]+[m2]+l[:]
print(l)
