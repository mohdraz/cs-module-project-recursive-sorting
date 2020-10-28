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


'''
1. In-place-quicksort
2. we're going to move things around in the passed-in array
We don't allocate any other arays. We just juggle elements around int he passed-in array.
'''


def quicksort_in_place(a):
    def quicksort_recursive(a, low, high):
        if low >= high:
            return
        p = low # pivot index
        
        # Partition Step
        for i in range(low, high):
            if a[i] < a[p]:
                # Swap elemtn i with item to right of pivot
                a[p+1], a[i] = a[i], a[p+1]
                # Swap pivot with element on its right
                a[p+1], a[p] = a[p], a[p+1]
        # At this point, the pivot is in its final spot, and the left and right
        # partitions need to be sorted
        quicksort_recursive(a, low, p)
        quicksort_recursive(a, p+1, high)
    quicksort_recursive(a, 0, len(a))
    return a

a = [5, 9, 3,10, 2, 3, 7, 2, 8, 1, 6]
print(f"Quick_Sort:\n   {quicksort_in_place(a)}\n{a} ")


