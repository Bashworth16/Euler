fib_list = [0, 1, 2]
stop_num = 4000000
even_fibs = []

#Builds the fibonacci sequence not exceeding 4 million.
def build_seq(x: list):
    while x[-1] < stop_num:
        n = x[-1]
        n += x[-2]
        x.append(n)


build_seq(fib_list)

#Creates new list of all even number in the fibonacci sequence.
def pull_even_fibs(xs: list):
    for x in xs:
        if x % 2 == 0:
            even_fibs.append(x)

pull_even_fibs(fib_list)
print('The sum of all even number in this sequence is ', sum(even_fibs))