def list_sum():
	b=input("Enter Elements of B : ")
	b=b.split(" ")
	int_b=[]
	for i in b:
		int_b.append(int(i))
	print("\nList B sums to ",sum(int_b))
	
list_sum()
