#1
def sum_div_by(n, stop):
    p = (stop-1) // n
    return n * p * (p+1) // 2

stop = 1000
print('#1:', sum_div_by(3, stop) + sum_div_by(5, stop) - sum_div_by(15, stop))


#2
def fib(stop):
	a, b = 0, 1
	while a < stop:
		yield a
		a, b = b, a + b
		
print('#2:', sum(x for x in fib(4000000) if x%2==0))


#3
from math import sqrt
from itertools import chain, count

def largest_prime_factor(n):
    for factor in chain([2], count(3, 2)):
        while(n % factor == 0):
            n //= factor
        if n == 1: 
            return factor
        if factor > sqrt(n):
            return n

print('#3:', largest_prime_factor(600851475143))


#4
from itertools import combinations

def is_pal(n):
    n = str(n)
    l = len(n)
    return n[:l//2] == n[l//2:][::-1]

print('#4:', max(a*b for a, b in combinations(range(1000), 2) if is_pal(a*b)))


#5
from functools import reduce
from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

print('#5:', reduce(lcm, range(1, 21)))


#6
print('#6:', sum(range(1, 101))**2 - sum(x*x for x in range(1, 101)))


#7
from math import sqrt

def is_prime(n):
    if n == 1:    return False
    if n < 4:     return True  # 2, 3
    if n % 2 ==0: return False
    if n < 9:     return True  # 5, 7
    if n % 3 ==0: return False
    else:
        root = int(sqrt(n))
        divisor = 5
        while divisor <= root:
            if n % divisor ==0:     return False
            if n % (divisor+2) ==0: return False
            divisor += 6
    return True

def nth_prime(stop):
	i = n =  0
	while n < stop:
		i += 1
		if is_prime(i):
			n += 1
	return i
	
print('#7:', nth_prime(10001))


#8
from functools import reduce

def n_adj_digits(n):
	data = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
	i = 0
	while i < len(data) - n + 1:
		yield data[i: i+n]
		i += 1

def product(s):
	return reduce(lambda a, b: int(a)*int(b), s)

print('#8:', max(product(n) for n in n_adj_digits(13)))


9
from functools import reduce
from math import sqrt
from operator import mul

def hyp(a, b):
	return sqrt(a**2 + b**2)

def py_triplet_less_than(stop):
	for a in range(stop//2, 0, -1):
		for b in range(stop//2, 0, -1):
			c = hyp(a, b)
			if a + b + c == 1000:
				return a, b, c

print('#9:', int(reduce(mul, py_triplet_less_than(1000))))


#10
from math import sqrt

def sum_primes(stop):
	# Sieve of Eratosthenes
  sieve = list(range(stop+1))
  sieve[1] = 0
  for n in range(2, int(sqrt(stop))+1):
      if sieve[n] > 0:
          for i in range(n*n, stop+1, n): 
          	sieve[i] = 0
  return sum(sieve)

print('#10:', sum_primes(2000000))