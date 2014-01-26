import math

def check(l1,l2):
	x = l1 * l2
	x_list = map(int,str(x))
	is_bad = False
	for i in range(len(x_list)):
		if x_list[i] != x_list[-i-1]:
			is_bad = True
	if not(is_bad):
		print l1,l2,x

list1 = [f for f in range(100,1000)]
print list1[899]
for i in range(100,list1[-1]-1):
    j = i+1
    while j > i and list1[j] < 999:
    	#print i,j, list1[i],list1[j]
    	check(list1[i],list1[j])
    	j += 1
