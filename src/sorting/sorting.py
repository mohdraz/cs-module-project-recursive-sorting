# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0
    # for k in range(len(merged_arr)+1):
    #     print(f"k: {k} ")
    #     if arrA[i] <= arrB[j]:
           
    #         merged_arr[k] = arrA[i]
    #         i += 1
    #     else:
    #         merged_arr[k] = arrB[j]
    #         j += 1

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            # merged_arr.append(arrA[i])
            i += 1
        else: 
            merged_arr[k] = arrB[j]
            # merged_arr.append(arrB[j])
            j += 1
        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i +=1
        k +=1 

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j +=1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    m = (len(arr)) // 2
    left = arr[:m]
    right = arr[m:]
    # print(f"left: {left} ")
    # print(f"right: {right} ")

    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    # print(f"left_arr: {left_arr} ")
    # print(f"right_arr: {right_arr} ")

    arr = merge(left_arr, right_arr)
  
    # merge(left, right)

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# merge_sort(arr1)

print(f"Result: {merge_sort(arr1)} ") # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

