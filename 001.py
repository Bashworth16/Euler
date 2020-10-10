total = 0

#Finds the sum total of all numbers divisable by 3 or 5 between 1 and 1 thousand.
for n in range(1, 1000):
    if n % 3 == 0:
        total = total + n
        continue
    if n % 5 == 5:
        total = total + 5

print(total)