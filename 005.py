"""Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

result = 1
START = 2
END = 20
num = 0
THE_RANGE = range(START, END + 1)
COMMON_MULTIPLES = {}

for x in THE_RANGE:
    result *= x    # To find the largest number divisible by each number in the range.

print(f'result = {result}')

for x in THE_RANGE:  # By setting the x and y loops directly inside each other,
    for y in THE_RANGE:  # we only change the denominator (x) if the quotient is no longer evenly divisible by each number in THE_RANGE
        q = result // y   # q is the quotient being checked by each number in THE_RANGE.
        ok = True         # This is my Flag check in order to update result and break out of the loop if the conditions are met.
        for i in THE_RANGE:  # This loop is to Check to see if the quotient is divisible by each number in THE_RANGE
            if q % i != 0:   # If not evenly divisible,
                ok = False   # Switch
                break        # break
        if ok and q < result:  # If we reach this point, then quotient is evenly divisible by all number in THE_RANGE and is the 'lesser' common multiple,
            result = q         # Update result with the "Lesser" common multiple.
            print('Reduced result to',result)

print('LCM =',result)
