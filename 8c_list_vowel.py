a=input("Enter a String : ")
b=[]
vowels="aeiouAEIOU"
for i in a:
    b.append(i)
print("List of Characters : ",b)
c=[x for x in b if x in vowels]
print("List of Vowels = ",c)
