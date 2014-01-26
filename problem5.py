import math

list1 = range(20,0,-1)
print list1

for i in range(20):
	tmp = list1[i] 
	j = 2
	while j <= list1[i]:
		if list1[i] % j == 0:
			list1[i] = list1[i] / j
			k = i+1
			while k < 20 :
				if list1[k] % j == 0:
					list1[k] = list1[k]/j
					print list1[i]
					print i,j,k, list1
				k += 1 
		if list1[i] % j != 0:
			j += 1 
	list1[i] = tmp
out = 1

for i in range(len(list1)):
	out = list1[i] * out
print out