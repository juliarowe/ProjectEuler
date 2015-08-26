#!

def nthFibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2

	return (nthFibonacci(n-1) + nthFibonacci(n-2))

def isEven(n):
	if n%2 ==0:
		return True
	else :
		return False

def sumEvenFib():
	tot = 0
	x = 1
	
	while (nthFibonacci(x) < 4000000):
		if isEven(nthFibonacci(x)):
			tot = tot + nthFibonacci(x)
		x = x + 1

	return tot

print sumEvenFib()