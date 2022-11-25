def noc():
	a=input("Enter A Sentence : ")
	b=[]
	for i in a:
		if i not in b:
			b.append(i)
	for i in range(0,len(b)):
		print(b[i]," repeats ",a.count(b[i])," times")
		

noc()
