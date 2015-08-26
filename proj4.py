#!

def isPal(num):
	
	temp = num
	revrs = 0

	while (temp > 0):
		firstDigit = temp % 10
		temp = temp/10
		revrs = revrs*10 + firstDigit

	if revrs == num :
		return True
	else :
		return False

biggestPal = 0

for x in xrange(999,100, -1) :
	for n in range(999,100, -1) :
		if (isPal(n*x) and (n*x > biggestPal)):
			biggestPal = n*x


print biggestPal