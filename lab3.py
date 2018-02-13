# Tyler deBoon 120030
# CMPT 460
import math

PRIME_LIST = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

def pseudo_prime(n, verbose = True):
	results = []
	divisible = False
	is_prime = False
	for a in PRIME_LIST:
		if a >= n:
			break
		if pow(a,n - 1, n) == 1 and a < n:
			results.append(a)
		if n % a == 0:
			divisible = True
	if len(results) and not divisible:
		is_prime = True
	if verbose:
		print "Checking", n
		print "\tPseudoprime to", results
		if divisible:
			print "\tIs divisible"
		if is_prime:
			print "\tProbably Prime"
		else:
			print "\tNot Prime"
	return is_prime, results
	
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def Carmichael():
	# im not cheating with these values I just know the next 5 carmichael numbers are between these values
	for n in xrange(1104,8912):
		is_prime, pseudo_results = pseudo_prime(n, False)
		if not is_prime and len(pseudo_results):
			# print "checking", n
			is_car = True
			for a in xrange(1,n):
				# print "range", a
				if gcd(a,n) == 1:
					if pow(a,n - 1,n) != 1:
						is_car = False
						break
			if is_car:
				print n

def c_number(number_of = 6, starting_place = 562, verbose = True):
	found_c_nums = []
	n = starting_place;
	while len(found_c_nums) < number_of:
		is_prime, pseudo_results = pseudo_prime(n, False)
		if not is_prime and len(pseudo_results):
			is_car = True
			for a in xrange(1,n):
				if gcd(a,n) == 1:
					if pow(a,n - 1,n) != 1:
						is_car = False
						break
			if is_car:
				found_c_nums.append(n)
		n += 1
	if verbose:
		print found_c_nums
	return found_c_nums
# broken does not work for prime numbers above 990ish will work for composite numbers larger though
def prime_factor(n, verbose = False):
	factors = []
	spinning = 0
	while n != 1 and spinning < 10000:
		for d in PRIME_LIST:
			if n % d == 0:
				n /= d
				factors.append(d)
				break
		spinning += 1
	if spinning > 10000:
		if verbose:
			print "Either the number entered has more than 10000 factors or its a prime number larger than this function can deal with"
		return []
	if verbose:
		print factors
	return factors

def find_7pqr():
	last_guess = 561
	while True:
		possible = c_number(1, last_guess, False)
		factors = prime_factor(possible[0])
		# if factors[0] == 7 and len(factors) == 4:
		if len(factors) == 4:
			# print "The first composite number with four prime factors including a 7"
			print possible[0]
			print factors
			return possible[0]
		last_guess = possible[0] + 1
	


pseudo_prime(7)
c_number(10)
find_7pqr()