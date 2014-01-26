import math
t = 2
sum = 0
while t < 2000000:
	is_prime = True
	for k in range(2,int(math.sqrt(t))+1,1):
		if t % k == 0:
			is_prime = False
	if is_prime :
		sum += t
		print t, sum
	t += 1