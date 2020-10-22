big_number = 600851475143

#finds prime factors in the given range.
for x in range(2, big_number //2):
    if x % 2 == 0:
        continue
    for t in range(2, x // 2):
        if x % t == 0:
            continue
    if big_number % x == 0:
        big_number = big_number / x
        if big_number == 1:
            print('Done! Your highest prime factor in 600,851,475,143 is', x)