# -*- coding:utf-8 -*-
phone_dict = {"EIGHT":0,"NINE":1,"ZERO":2,"ONE":3,"TWO":4,"THREE":5,"FOUR":6,"FIVE":7,"SIX":8,"SENVE":9}
output = []
#          O&!Z&!W&!R ->3  对O进行计数，减去Z,W,R，如果有多的O就是3

# G->0  Z->2  W->4   U->6  X->8

#H&!G ->5      !U&F->7    S&!X ->9

n = int(raw_input())
for i in range(n):
	phone_number = {}
	random_phone_number = raw_input()
	count = {}
	for j in range(len(random_phone_number)):
		if count.has_key(random_phone_number[j]):
			count[random_phone_number[j]] = count[random_phone_number[j]]+1
		else:
			count[random_phone_number[j]] = 1
	if count.has_key("G") and count["G"]>0:    #判断有没有0   独立
		count["E"] = count["E"] - count["G"]
		count["I"] = count["I"] - count["G"]
		count["T"] = count["T"] - count["G"]
		count["H"] = count["H"] - count["G"]
		phone_number[0] = count["G"]
	if count.has_key("Z") and count["Z"]>0:   #判断有没有2    独立
		count["E"] = count["E"] - count["Z"]
		count["R"] = count["R"] - count["Z"]
		count["O"] = count["O"] - count["Z"]
		phone_number[2] = count["Z"]
	if count.has_key("W") and count["W"]>0:   #判断有没有4   独立
		count["T"] = count["T"] - count["W"]
		count["O"] = count["O"] - count["W"]
		phone_number[4] = count["W"]
	if count.has_key("U") and count["U"]>0:   #判断有没有6   独立
		count["F"] = count["F"] - count["U"]
		count["O"] = count["O"] - count["U"]
		count["R"] = count["R"] - count["U"]
		phone_number[6] = count["U"]
	if count.has_key("X") and count["X"]>0:   #判断有没有8  独立
		count["S"] = count["S"] - count["X"]
		count["I"] = count["I"] - count["X"]
		phone_number[8] = count["X"]
	if count.has_key("H") and count["H"]>0:   #判断有没有5
		count["T"] = count["T"] - count["H"]
		count["R"] = count["R"] - count["H"]
		count["E"] = count["E"] - 2*count["H"]
		phone_number[5] = count["H"]
	if count.has_key("F") and count["F"]>0:   #判断有没有7
		count["I"] = count["I"] - count["F"]
		count["V"] = count["V"] - count["F"]
		count["E"] = count["E"] - count["F"]
		phone_number[7] = count["F"]
	if count.has_key("S") and count["S"]>0:   #判断有没有9
		count["E"] = count["E"] - 2*count["S"]
		count["N"] = count["N"] - count["S"]
		count["V"] = count["V"] - count["S"]
		phone_number[9] = count["S"]
	if count.has_key("I") and count["I"]>0:   #判断有没有1
		count["N"] = count["N"] - 2*count["I"]
		count["E"] = count["E"] - count["I"]
		phone_number[1] = count["I"]
	if count.has_key("O") and count["O"]>0:   #判断有没有1
		count["N"] = count["N"] - 2*count["O"]
		count["E"] = count["E"] - count["O"]
		phone_number[3] = count["O"]
	k = ""
	for t in xrange(10):
		if phone_number.has_key(t):
			for n in xrange(phone_number[t]):
				k = k+str(t)
	output.append(k)

for i in xrange(len(output)):
	print output[i]