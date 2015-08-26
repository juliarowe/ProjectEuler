#!

def isPal(num):
	l = []
	r = []

	while num > 0:  
		l.append(num%10)
		r.append(num%10)
		num = num/10

	l.reverse()

	return l == r

answer = 0
found = False

for i in xrange(999, 100, -1):
	if found:
		break
	for j in xrange (999, 990, -1):
		if isPal(i*j):
			found = True
			answer = i*j
			break


print answer
print i 
#print j



