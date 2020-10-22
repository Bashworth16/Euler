"""A palindromic number reads the same both ways.
  The largest palindromic number made from the product of
  two 2-digit number is 9009 = 91 X 99.

  Find the largest palindrome made from the product of two 3-digit numbers."""

pal = 0

#Finds highest Palindrome Products.
for x in range(1000, 100, -1):
    for i in range(1000, 100, -1):
        if str(x * i)[::-1] == str(x * i) and x * i > pal:
            print(x, i)
            pal = x * i

print('Done!', pal)

