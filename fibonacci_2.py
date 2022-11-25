def Fib(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fib(n-1) + Fib(n-2))  
term = int(input("Enter the terms? "))
  
if term <= 0:  
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(term):  
       print(Fib(i))


