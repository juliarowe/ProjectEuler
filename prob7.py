#!
import time
start = time.time()

def isPrime(num):
	for x in xrange (num/2, 1, -1) :
		if (num%x == 0) :
			return False

	return True

thatPrime = 0
stop = 2000


for x in xrange(2, 10000000000) :
	if stop <= 0:
		break
	if isPrime(x) :
		thatPrime = x
		stop = stop - 1


print thatPrime

print 'It took', time.time()-start, 'seconds.'