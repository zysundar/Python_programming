def recur_sum(num):
   """Function to return the sum
   of natural numbers using recursion"""
   if num <= 1:
       return num
   else:
       return num + recur_sum(num-1)

# take input from the user
num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
