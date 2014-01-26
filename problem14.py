n = 13
max_c = 0
max_n = 0
while n < 1000000:
	k = n
	count = 1
	while k > 1 : 
		k = k/2 if k % 2 == 0 else 3*k+1
		count +=1
	if count > max_c:
		max_c = count
		max_n = n
		print max_n
	n += 1
print max_c, max_n

