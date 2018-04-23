# sentence = raw_input()

# word = sentence.split(" ")

# output = word[0]
# for i in range(len(word)):
# 	if i!=0:
# 		output = output+"%20"+word[i]
# print output


sentence = raw_input()

output = ""
for i in range(len(sentence)):
	if not sentence[i]==" ":
		output = output+sentence[i]
	else:
		output = output+"%20"
print output