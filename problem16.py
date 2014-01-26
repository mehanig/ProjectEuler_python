n = 1
for i in range(1000):
	n = n * 2

print n
nstr = str(n)
sum = 0
for i in range(len(nstr)):
	sum += int(nstr[i])
print sum

#print(sum(int(c) for c in str(2**1000)))
