'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

primes = {1: 2}  # I started the dictionary with {1: 2} because the first one is a given and much less of a headache if I declare it here.
END = len(primes.keys())  # I Created an "END" variable for the length of the keys in my dictionary so I could tell the loop to stop when the length reaches a desired number.
num = 3  # Start my number count at 3 saved as num, this should be the 2nd Key added to my dictionary. e.x. {1: 2, 2: 3}.
k = 2  # This is my Key Count variable so when I find a prime number, i can assign it a Key number and add it to my dictionary.

while END != 6:  # I expect this to loop until END (the length of keys in my primes dictionary) reaches 6.
    print(f'num = {num}')  # To help me track what number we are examining in the loop
    for x in range(2,num//2):  # This checks to see if num is divisible by any number besides 1 and its self, and thus NOT a prime number...
        if num % x == 0:  # If its not a prime number...
            num += 1       # ... add 1 to num
            break           # ... Start loop again
        if num % x != 0:    # If it is a prime...
            primes[k] = num # ... Append to dictionary
            print(primes)
            num += 1          # ... add 1 to num
            k += 1             # ... add 1 to k

