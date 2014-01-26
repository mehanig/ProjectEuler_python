f = open("C:/Users/MAfanasyev/Dropbox/Public/Python/names.txt")
lines = f.read().replace(',',' ').replace('"',' ' ).split()
f.close()
lines.sort()

dict_abc = {'A' : 1, 'B': 2 , 'C': 3, 'D': 4, 'E':5, 'F':6, 'G':7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12,	'M' : 13, 'N' : 14,\
			'O': 15, 'P': 16, 'Q':17, 'R' :18, 'S' : 19, 'T':20, 'U':21, 'V':22, 'W': 23, 'X' : 24,	'Y' : 25, 'Z' : 26}
#print lines[]
added = 0
for line in range(len(lines)):
	summ = 0
	for k in range(int(lines[line].__len__())):
		summ += dict_abc[lines[line][k]]
	print summ
	added += summ * (line+1)
	print added
	#lines[line].append(summ)
