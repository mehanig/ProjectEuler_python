import math
t = 14
i = 7
while i <= 10001:
	is_prime = True
	for k in range(2,int(math.sqrt(t))+1,1):
		if t % k == 0:
			is_prime = False
	if is_prime :
		print i, t
		i +=1
	t += 1