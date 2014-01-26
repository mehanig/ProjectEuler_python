import math 

divis = 1

def divis_quantity(num):
	out = 0
	for i in range(1, int(math.sqrt(num))+1):
		if num % i == 0:
			out += 2
	return out

num = 1
i = 1
while divis < 501:
	i +=1 
	num = num + i
	divis = divis_quantity(num)
	print num, divis

