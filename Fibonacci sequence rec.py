def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
      return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = int(input("How many terms? "))
if nterms <= 0:
   print("Plese enter a positive integer")
else:
  # print("Fibonacci sequence:",recur_fibo(nterms))
   for i in range(nterms):
       print(recur_fibo(i))

