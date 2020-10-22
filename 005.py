"""Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

result = 1
START = 2
END = 10
num = 0
THE_RANGE = range(START, END + 1)
COMMON_MULTIPLES = {}

for x in THE_RANGE:
    result *= x    # To find the largest number divisible by each number in the range.

print(result)

# Write While loop to reduce result to the Least Common Multiple for each number in the range...
for x in THE_RANGE:
    q = result // x
    print(f'{result} // {x} = {q}')
    ok = True
    for y in THE_RANGE:
        if q % y != 0:
            ok = False
            break
    if ok:
        result = q
        print('Reduced result to ', result)

print(result)


