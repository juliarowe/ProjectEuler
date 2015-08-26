p_list = []

for x in xrange(3, 2000000, 2):
	p_list.append(x)

def removeNum(n, p_list):
	for x in xrange(0,len(p_list)):
		if isFactor(p_list[x], n) :
			p_list.pop([x])

def isFactor(num, fact):
	if num % fact == 0:
		return True
	else :
		return False

def isPrime(num):

	for x in xrange(2, num/2):
		if (isFactor(num, x)):
			return False

	return True

sumOfprimes = 2

while len(p_list) > 0:
	if isPrime(p_list[0]) :
		sumOfprimes = sumOfprimes + p_list[0]
		removeNum(p_list[0], p_list)
	else :
		p_list.pop([0])

print sumOfprimes