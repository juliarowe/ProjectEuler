#!
#incredibly slow...

import time
start = time.time()

def isFactor(num, fact):
	if num % fact == 0:
		return True
	else :
		return False

def isPrime(fact):

	for x in xrange(2, fact/2):
		if (isFactor(fact, x)):
			return False

	return True

thisNum = 600851475143
largestPfact = 0


for x in xrange(thisNum/2, thisNum/2 - 1000, -2):
	print x
	if isFactor(thisNum, x) and isPrime(x):
		largestPfact = x
		found = True
		break


print largestPfact
print 'It took', time.time()-start, 'seconds.'
