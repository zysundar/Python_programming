'''graph={'A':['E','B','D']
       'B':['C','D','E']
       'C':['A','B']
       }'''
#------------------fabonoiciii series-------------------
fibtable={}
def fib(n):
    fibtable[0]=0
    fibtable[1]=1
    for i in range(2,n+1):
        fibtable[i]=fibtable[i-1]+fibtable[i-2]
    return fibtable[n]
print fib(8)
print fibtable

#---------------------factorial-------------------
fact={}
fact[0]=1
fact[1]=1
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        for i in range(2,n+1):
            fact[i]=i*fact[i-1]
        return fact[i]
print factorial(1)
print fact

#------------------binary search--------------------
'''def binarysearch(list1,item):
    list1copy=sorted(list1)
    n=len(list1copy)
    beg=0
    end=n-1
    mid=(beg+end)/2'''
    
