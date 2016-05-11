
# Project Euler
'''
My solutions to Project Euler in python

#1
print '#1:', sum(x for x in xrange(1, 1000) if x%3==0 or x%5==0)


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
		
print '#2:', sum(x for x in fib(4000000) if x%2==0)


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

print '#3:', largest_prime_factor(600851475143)


#4
def is_palindrome(n):
	n = str(n)
	for x in xrange(len(n)/2+1):
		if n[x] is not n[-x-1]:
			return False
	else:
		return True

print '#4:', max(i*j for i in xrange(1000) for j in xrange(1000) if is_palindrome(i*j))


#5
from fractions import gcd

def lcm(a, b):
    return (a * b) / gcd(a, b)

print '#5:', reduce(lcm, xrange(1, 21))


#6
print '#6:', sum(xrange(1, 101))**2 - sum(x*x for x in xrange(1, 101))


#7
def nth_prime(stop):
	i = 0
	n = 0
	while n < stop:
		i += 1
		if is_prime(i):
			n += 1
			#print i, n
	return i
	
print '#7:', nth_prime(10001)

#8
def n_adj_digits(n):
	data = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
	i = 0
	while i < len(data) - n + 1:
		yield data[i: i+n]
		i += 1

from operator import mul

print '#8:', max(reduce(mul, list, 1) for n in n_adj_digits(13))


#9
def hyp(a, b):
	from math import sqrt
	return sqrt(a**2 + b**2)

def py_triplet_less_than(stop):
	for a in range(stop/2, 0, -1):
		for b in range(stop/2, 0, -1):
			c = hyp(a, b)
			if a + b + c == 1000:
				return a, b, c

from operator import mul
print '#9:', reduce(mul, py_triplet_less_than(1000))
'''

#10

print '#9:',

