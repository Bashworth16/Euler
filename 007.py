'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

primes = {1: 2}
END = len(primes.keys())
num = 3
k = 2

while END != 6:
    print(f'num = {num}')
    for x in range(2,num//2):
        if num % x == 0:
            num += 1
        if num % x != 0:
            primes[k] = num
            num += 1
            k += 1



