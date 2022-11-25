def fact():
	a=int(input("Enter a number to find factorial:"))
	f=1
	for i in range(1,a+1):
        	f*=i
	print("the factorial of the given number is ",f)

fact()
