def main():
 # Write code here 
    n=int(input())
    k=[]
    count=0
    sum1=0
    k=list(map(int,input().split()))
    l=set(k)
    for i in l:
        print("i",i)
        for j in k:
            print("j",j)
            if(i==j):
                count=count+1
        if(count>1):
            sum1=sum1+i
        count=0
    print("sum",sum1)
main()
