def omg(*args):
	for i in args:
		print i

if __name__ == '__main__':
    print "ok"
    k = ["a", "b","c"]
    for i,j in enumerate(k):
    	print ('{},{}'.format(i,j))
    print dict(enumerate(k))
    l = ["1",2,"6"]
    x = [omg(i) for i in l]
    print "this is", x