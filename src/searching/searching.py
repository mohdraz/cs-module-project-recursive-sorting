# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    print(f"start: {start} end: {end} ")
    # arr.sort()

    if end >= start:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, len(arr) - 1)
        else:
            return binary_search(arr, target, 0, mid-1)
    else:
        return -1


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# print(binary_search(arr1, -81, 0, len(arr1)-1))  # return 1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    high = len(arr) -1
    low = 0


    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            globals()['pos'] = mid
            return mid
        else:
            if arr[mid] < target:
                if arr[low] > arr[high]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if arr[low] > arr[high]:
                    low = mid + 1
                else: 
                    high = mid -1
    return -1

ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
print(f"result: {agnostic_binary_search(ascending, 12)} ") # return 2
print(f"result: {agnostic_binary_search(descending, 49)} ") # return 3

# while low <= high:
#         print(f"low: {low} high: {high} ")
#         mid = (low+high) // 2
#         print(f"mid: {mid} ")
#         if arr[mid] == target:
#             globals()['pos'] = mid
#             return mid
#         else:
#             if arr[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#     return -1