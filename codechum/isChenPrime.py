def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isSemiPrime(n):
    prime_fact = 0

    start = 2
    while n > 1:
        if n % start == 0 and isPrime(start):
            n /= start
            prime_fact += 1
        else:
            start += 1

    return prime_fact == 2

size = int(input("Enter size: "))

list = []

for i in range(size):
    list.append(int(input()))

for i in list:
    print(i, end=" ")

    if isPrime(i) and (isSemiPrime(i + 2) or isPrime(i + 2)):
        print("YES")
    else:
        print("NO")

