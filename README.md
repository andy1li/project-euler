
# Project Euler

My solutions to Project Euler in python

```python
#1
print '#1:', sum(x for x in xrange(1, 1000) if x%3==0 or x%5==0)


#2
def fib(stop):
	a, b = 0, 1
	c = a + b
	while c < stop:
		yield c
		a, b = b, c
		c = a + b
		
print '#2:', sum(x for x in fib(4000000) if x%2==0)


#3
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n))+2, 2))

def largest_prime_factor(n):
	for x in xrange(int(sqrt(n))+1, 0, -1):
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
	i = n =  0
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

def product(s):
	return reduce(lambda a, b: int(a)*int(b), s)

print '#8:', max(product(n) for n in n_adj_digits(13))


#9
from math import sqrt

def hyp(a, b):
	return sqrt(a**2 + b**2)

def py_triplet_less_than(stop):
	for a in range(stop/2, 0, -1):
		for b in range(stop/2, 0, -1):
			c = hyp(a, b)
			if a + b + c == 1000:
				return a, b, c

from operator import mul
print '#9:', int(reduce(mul, py_triplet_less_than(1000)))


#10
from math import sqrt

def sum_primes(stop):
	# Sieve of Eratosthenes
  sieve = range(stop+1)
  sieve[1] = 0
  for n in xrange(2, int(sqrt(stop))+1):
      if sieve[n] > 0:
          for i in xrange(n*n, stop+1, n): 
          	sieve[i] = 0
  return sum(sieve)

print '#10:', sum_primes(2000000)


#11

import numpy as np
from itertools import imap as map, chain 

data = np.array([[8, 2, 22, 97, 38, 15, 0, 4, 0, 75, 4, 5, 7, 78, 52, 12, 5, 77, 91, 8],
					 	 	   [49, 49, 99, 4, 17, 81, 18, 57, 6, 87, 17, 4, 98, 43, 69, 48, 4, 56, 62, 0],
								 [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 4, 67, 53, 88, 3, 3, 49, 13, 36, 65],
								 [52, 7, 95, 23, 4, 6, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
								 [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 4, 4, 28, 66, 33, 13, 8],
								 [24, 47, 32, 6, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 2, 35, 17, 12, 5],
								 [32, 98, 81, 28, 64, 23, 67, 1, 26, 38, 4, 67, 59, 54, 7, 66, 18, 38, 64, 7],
								 [67, 26, 2, 68, 2, 62, 12, 2, 95, 63, 94, 39, 63, 8, 4, 91, 66, 49, 94, 21],
								 [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
								 [21, 36, 23, 9, 75, 0, 76, 44, 2, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
								 [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 8, 4, 62, 16, 14, 9, 53, 56, 92],
								 [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
								 [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 6, 21, 58, 51, 54, 17, 58],
								 [19, 8, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 4],
								 [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
								 [88, 36, 68, 87, 57, 62, 2, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
								 [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 4, 62, 76, 36],
								 [2, 69, 36, 41, 72, 3, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
								 [2, 73, 35, 29, 78, 31, 9, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
								 [1, 7, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]])

def diags(data):
	height, width = data.shape
	diags = (data.diagonal(i) for i in xrange(-height+1, width))
	diags = chain(diags, (np.rot90(data).diagonal(i) for i in xrange(-width+1, height)))
	return diags

def product_four(line):
	if len(line) < 4:
		return ()

	def mul_four(i, x):
		if i+4 > len(line):
			return -float('inf')
		else:
			#print 'four:', line[i], line[i+1], line[i+2], line[i+3]
			return line[i] * line[i+1] * line[i+2] * line[i+3]

	return (mul_four(i, x) for i, x in enumerate(line))

all_directions  = chain(data, data.T, diags(data))
nested_products = map(product_four, all_directions)
products        = chain.from_iterable(nested_products)

print '#11:', max(products)
```