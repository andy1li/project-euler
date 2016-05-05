# Project Euler
My solutions to Project Euler in python

```
#1
print sum(x for x in xrange(1, 1000) if x%3==0 or x%5==0)

#2
def fib(stop):
	a = 0
	b = 1
	c = a + b
	while c < stop:
		yield c
		a = b
		b = c
		c = a + b
		
print sum(x for x in fib(4000000) if x%2==0)

#3
import math

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n))+2, 2))

def largest_prime_factor(n):
	for x in xrange(int(math.sqrt(n))+1, 0, -1):
		if n%x == 0 and is_prime(x):
			return x

print largest_prime_factor(600851475143)

#4
def is_palindrome(n):
	n = str(n)
	for x in xrange(len(n)/2+1):
		if n[x] is not n[-x-1]:
			return False
	else:
		return True

print max(i*j for i in xrange(999, 0, -1) for j in xrange(999, 0, -1) if is_palindrome(i*j))

#5
def is_evenly_divisible(n, to):
	for x in range(2, to+1):
		#print x, n/x, n%x
		if n%x != 0:
			return False
	else:
		return True

# first try is_evenly_divisible(2520*11*13*17*19, 20)
# fail case: divided by 16 equals 8, so multiple by 2 and try again
print is_evenly_divisible(2520*11*13*17*19*2, 20)

#6
def solve_6(n):
	return sum(xrange(1, n+1))**2 - sum(x*x for x in xrange(1, n+1))
	
print solve_6(100)

#7
def nth_prime(stop):
	i = 0
	n = 0
	while n < stop:
		i+=1
		if is_prime(i):
			n+=1
			#print i, n
	return i
	
print nth_prime(10001)

```
