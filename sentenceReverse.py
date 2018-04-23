n = raw_input()
one_words = n.split(" ")
i = len(one_words)-1
while i>0:
	print(one_words[i]),
	i = i-1
print(one_words[0]),