string = raw_input("Enter a word to check if it's a palindrome:\n")
if string==string[::-1]:
	print "Yes, it's a palindrome!"
else:
	print "Nope, not a palindrome."