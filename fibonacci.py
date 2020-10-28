# 0 1 2 3 4 5 6 7  8  9  10 ... <- index
# 0 1 1 2 3 5 8 13 21 34 55 ... <- Fibonacci number
# ^^^
# base cases
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)

cache = {}


def fib_adv(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n <= 1: return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

# for i in range(1000000000):
#     print(f"{i}: {fib(i)} ")

# 0 1 2 3 4 5 6 7  8  9  10 ... <- index
# 0 1 1 2 3 5 8 13 21 34 55 ... <- Fibonacci number
# ^^^
# base cases
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)
# Regular Fibanochi


def fib(n):
    # Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n <=1: return n
    return fib(n-1) + fib(n-2) # O(2^n)

for i in range(10):
    print(f'{i}: {fib(i)} ')
