"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

THE_RANGE = range(1, 600)

# The first three loops for a, b, and c are to compare numbers within the range to find pythagorean triplets whil following the 'a > b > c' rule.

for a in THE_RANGE:
    for b in THE_RANGE:
        if a >= b:
            continue
        for c in THE_RANGE:
            if b >= c:
                continue

            # This first if statement is to narrow the search results.

            if (a + b + c) < 1000:
                continue

            # Confirm a, b, and c make a pythagorean triplet.

            if (a**2 + b**2) == c**2:
                print(f'a is {a}, b is {b}, c is {c}')
                print(f'a + b + c = {a+b+c}')
                print(f'a2({a**2}) + b2({b**2}) = {a**2 + b**2}, c2 = {c**2}')
                print('')

                # Find a, b, and c that total 1000.

                if (a + b + c) == 1000:
                    print(f'FOUND!!! {a} + {b} + {c} = 1000')
                    print(f'The product of a({a}) * b({b}) * c({c}) is {a*b*c}')
            break
