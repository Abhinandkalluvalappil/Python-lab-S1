def pyramid():
	n=int(input("Enter a number for building a pyramid:"))
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(i*j,end=" ")
			n=n+1
		print("\r")
pyramid()
