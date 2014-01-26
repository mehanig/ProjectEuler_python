import math

max_out = []
i = 3
number = 600851475143
while (i < math.sqrt(number)):
	if number % i  == 0 :
		max_out.append(i)
		print max_out
		number = number / i		
	i += 1	
max_out.append(600851475143 / max_out[-1])
print max_out
