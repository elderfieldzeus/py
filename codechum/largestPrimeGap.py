def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

size = int(input("Enter array size: "))
elems = list(map(int, input("Enter the numbers: ").split()))

primes = sorted([prime for prime in elems if isprime(prime)])

gap = 0
largest_pair = (0, 0)

for i in range(1, len(primes)):
    if primes[i] - primes[i - 1] > gap:
        gap = primes[i] - primes[i - 1]
        largest_pair = (primes[i - 1], primes[i])

if len(primes) < 2:
    print("Not enough primes to form a gap.")
else:
    print("Largest gap is: {} between primes {} and {}".format(gap, largest_pair[0], largest_pair[1]))