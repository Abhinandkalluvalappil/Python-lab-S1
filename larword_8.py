def large():
	str = input("Enter a String: ")
	word_list = str.split()
	longest_word = max(word_list, key = len)
	print("Longest word: ",longest_word)
large()
