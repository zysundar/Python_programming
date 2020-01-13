
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


