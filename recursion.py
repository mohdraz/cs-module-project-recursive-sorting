def print_nums(x, y):
    # if x < y:
    #     print(x)
    #     foo(x+1, y)
    # Base Case
    if x >= y:
        return

    print(x)
    print_nums(x+1, y)


print_nums(1, 3)

'''
can we define this problem in terms of identical subproblems? 

Goal: print the numbers from x to y-1
    print x
    print number fro x+1 to y-1
'''


'''
fibonacci sequence:

1. 0 1 1 2 3 5 8 13 21 34 55........
2. 0 1 1 2 3 5 8 13 21 34 55

fib(6):
    fib(5) + fib(4)

fib(0): --> 0
fib(1): --> 1

fib(n):
    fib(n-1) + fib(n-2)
'''


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n <= 1: return n
    return fib(n-1) + fib(n-2)  # O(2^n)

# print(fib(10))
# for i in range(100):
#     print(f'{i}: {fib(i)} ')


'''
quicksort(a):
    ...
    ...
    quicksort(...)

Partitioning in quicksort:
    choose a number to be the _pivot_
        let's choose teh the first number
    split the list into two lists:
        one with the number less than pivot
        the other with numbers greater than or eques to the privot
    put the smaller numbers left of the pivot
    greater numbers right of the pivot

    quicksort(left)
    quicksort(right)
'''


def partition(a):
    left = []
    pivot = a[0]
    right = []

    for v in a[1:]:
        if v < pivot:
            left.append(v)
        else:
            right.append(v)
    return left, pivot, right


def quicksort(a):
    if len(a) <= 1:
        return a
    left, pivot, right = partition(a)
    return quicksort(left) + [pivot] + quicksort(right)

# print(quicksort([5,9,2,10,12]))
