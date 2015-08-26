#!

def areFactors(num):

	for x in xrange(21, 10, -1):
		if num%x !=0:
			return 0

	return num

smallest = 0
startAt = 2520

while smallest == 0:
	smallest = areFactors(startAt)
	startAt = startAt + 10

print smallest