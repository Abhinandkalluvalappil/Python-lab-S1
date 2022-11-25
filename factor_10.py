def factor():
	num=int(input("Enter a number to find all factorial:"))
	i = 1
	print ("The factors of ",num," are: ")
	while i <= num :
		if (num % i==0) :
			print (i,end=" ")
		i = i + 1		
	
factor()


