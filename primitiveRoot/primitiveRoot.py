
def prime_factorization(n):
	result = {}
	while (n/2).is_integer():
		n = n/2
		if 2 in result:
			result[2] += 1
		else:
			result[2] = 1
	i = 3
	while n > 1:
		while (n/i).is_integer():
			n = n/i
			if i in result:
				result[i] += 1
			else:
				result[i] = 1
		i += 2
		if i > n:
			break
	if len(result) == 0:
		result[n] = 1 #prime number
	return result

	"""Euler's Totient function"""
def phi(n):
	primes = prime_factorization(n)
	result = n
	for prime in primes.items():
		result *= (1 - 1/prime[0])
	return int(result)
	
def find_primitive_root_given_one(n, root):
	pass
	
def find_primitive_roots(n):
	pass

if __name__ == "__main__":
	n = int(input("Type in the number for which you want to know the primitive roots:"))
	roots = find_primitive_roots(n)
	print(roots)