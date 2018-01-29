import math

def smallest_divisor(n):
	start = 2
	while start <= n:
		if n % start == 0:
			return start
		start += 1
	return n


def factors(n):
	if n < 2:
		return []
	else:
		factor = [smallest_divisor(n)]
		return factor + factors(n // smallest_divisor(n))


def pow_mod(base, exponent, mod):
	# fix base 2 detection
	base_two_power = math.floor(math.log(exponent)/math.log(2))
	# base_two_check = math.ceil(math.log(exponent)/math.log(2))
	# error checking to make sure the exponent is base two
	# if base_two_power != base_two_check:
	# 	# change this to have proper error throwing
	# 	print("Error: exponent must be base two", exponent, base_two_power, base_two_check)
	# 	return
	return _pow_mod(base, mod, base_two_power)


def _pow_mod(base, mod, count):
	if count < 1:
		return base
	else:
		base = base**2 % mod
		return _pow_mod(base, mod, count - 1)


def largest_base_two(exponent):
	return 2**math.floor(math.log(exponent) / math.log(2))


def modular_exponentiation(base, exponent, mod):
	if exponent < 1:
		return 1
	else:
		largest_exponet = largest_base_two(exponent)
		return pow_mod(base, largest_exponet, mod) * modular_exponentiation(base, exponent - largest_exponet, mod) % mod


def repeated_squares(base, exponent, mod):
	counter, answer = _rsh(exponent, mod, base, 1)
	return answer


def _rsh(exponent, mod, lastAns, power):
	if power * 2 > exponent:
		return exponent - power, lastAns ** 2 % mod
	else:
		if power == 1:
			lastAns = lastAns % mod
		else:
			lastAns = lastAns ** 2 % mod
		workingExponent, total = _rsh(exponent, mod, lastAns, power * 2)
		if workingExponent >= power:
			return workingExponent - power, total * lastAns % mod
		else:
			return workingExponent, total


def test_pow_mod():
	for x in range(0, 500):
		base = 5
		exponent = 2**x
		mod = 101
		if pow_mod(base, exponent, mod) != pow(base, exponent, mod):
			print("pow_mod test failed", x, pow(base, exponent, mod))
			return


test_pow_mod()


# print(modular_exponentiation(125,300,201))          #193
# print(modular_exponentiation(125,301,201))          #5
# print(modular_exponentiation(33,128,57))            #6
# print(modular_exponentiation(3333,4444,100))        #21
# print(modular_exponentiation(2,75,33))              #32
# print(modular_exponentiation(15,4,71))              #2
# print(modular_exponentiation(11,11,18))             #5
# print(modular_exponentiation(5478862,2256689,5214)) #4018