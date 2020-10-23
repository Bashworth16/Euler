"""he sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + 3^2... 10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + 3... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is, 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

sum = 0
START = 1
END = 100
THE_RANGE = range(START,END+1)

for x in THE_RANGE:  # totals the sum of squares of all numbers in THE_RANGE
    sum += x**2

print(sum)

s_of_sum = 0

for i in THE_RANGE:   # Gets the sum of all numbers in THE_RANGE
    s_of_sum += i

s_of_sum **= 2  # Squares the sum of THE_RANGE

diff = s_of_sum - sum  # Finds the difference

print(diff)