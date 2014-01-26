def test_func(numb):
    value = 0
    for i in range(len(str(numb))):
        value += int(str(numb)[i])**5
    if value == numb:
        print value
        return value
    else:
        return 0

summ= 0
i = 2
while i < 9999999:
    x = test_func(i)
    if test_func(i):
        summ +=i
        print i
    if (i% 10000 == 0):
        print i
    i+=1
print summ
