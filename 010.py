"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

THE_RANGE = range(3, 20)
the_sum = 2
is_prime = True

for x in THE_RANGE:
    if x % 2 == 0:
        is_prime = False
        continue
    for i in range(2, x):
        if x % i == 0:
            print(f'{x} FAIL 2.')
            print("")
            break
    if x % 2 != 0 and is_prime:
        the_sum += x
        print(f'x is {x}')
        print(f'the_sum is {the_sum}')
