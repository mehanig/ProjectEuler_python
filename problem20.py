fact = 1
n = 100
while n > 1:
	fact *= n
	n -= 1

print fact
out = 0
for i in range(len(str(fact))):
	out += int(str(fact)[i])
print out