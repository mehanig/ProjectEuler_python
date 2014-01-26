from math import sqrt

def prime_div(n):
	sumx = 1
	for i in range(2,int(sqrt(n))+1):
		if n % i == 0:
			sumx += ((n / i) + i)
	return sumx
sumx = 0

# print prime_div(220)
# print prime_div(284)
# print prime_div(prime_div(220))
i = 220
x = prime_div(i)
y = prime_div(x)
print x,y
i = 2
x = 0
y = 0
while i < 10000:
	x = prime_div(i)
	y = prime_div(x)
	if y == i and x > 1 and x != y:
		sumx = sumx + x + y
		print x, y , sumx/2
	i +=1

