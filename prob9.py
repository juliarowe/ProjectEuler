#!

def isTriplet(a, b, c):
	if ((a*a) + (b*b) == (c*c)):
		return True
	else: return False

def sum1000(a, b, c):
	if (a + b + c == 1000):
		return True
	else: return False

found = False

for a in xrange	(2, 1000, 1):
	if found:
		break
	for b in xrange	(3, 1000, 1):
		for c in xrange	(4, 1000, 1):
			if (a < b) and (b < c) and sum1000(a, b, c) and isTriplet(a, b, c):
				print a*b*c
				found = True
				break