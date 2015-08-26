#!

l = [1]
SumOfSquares = 1
Sum = 0
SquareOfSum = 0

for x in xrange(2,101):
	SumOfSquares = SumOfSquares + x*x
	l.append(x)

Sum = sum(l)

SquareOfSum = Sum*Sum

print SumOfSquares
print SquareOfSum

print SquareOfSum - SumOfSquares