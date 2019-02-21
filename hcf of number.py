def hcf(x, y):
   """This function takes two
   integers and returns the H.C.F"""
   if x > y:
       smaller = y
   else:
       smaller = x

   for i in range(2,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
        return i
       else:
          return 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))
