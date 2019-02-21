def main():
    a=int(input())
    for i in range(1,a+1):
        d_i = raw_input().split()
        d_i = list(d_i)
        d_i = map(int, d_i)
        b_i=raw_input()
        b_i=set(b_i)
    for i in range(1,a+1):
        s=sum(d_i)
        b=sum(ord(ch) for ch in b_i)
        print(s-b)
        
main()
