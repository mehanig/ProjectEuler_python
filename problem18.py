yy = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".replace(" ","").replace("\n","")

print yy
# numb = [[0 for x in range(15)] for y in range(15)]
# k = 0
# row = 0

# for j in range(15):
#     for i in range(i+1):
#         numb[i][j] = int(yy[i*2]+yy[i*2+1]
counter = 0
row = range(15)
for line in row:
    line_new = []
    for k in range(line+1):
        line_new.append(int(yy[counter]+yy[counter+1]))
        counter +=2
    #     row[line][k] = int(yy[i])
    row[line] = line_new

print row
way = []
thetta = 0
kappa = 0
x1 = 0
y1 = 0

for k in reversed(range(15-1)):
	for i in range(k+1):
		if row[k+1][i] > row[k+1][i+1]:
			row[k][i] += row[k+1][i]
		else:
			row[k][i] += row[k+1][i+1]
	print row[k]