def loop():
	n=5
	i=1;j=0
	while(i<=n):
		while(j<=i-1):
			print("* ",end="")
			j+=1
		print("\r")
		j=0;i+=1
	i=4;j=0
	while(i>=0):
		while(j<=i-1):
			print("* ",end="")
			j=j+1
		print("\r")
		j=0;i=i-1
loop()

	
	

