'''
Merge Sort is a divide and conqure algorithm.It's a comparison based algorithm
with time complexity O(N-logN).It's not a inplace algorithm and need additional
memory for sorting.
'''
def merge_sort(array):
    if len(array) == 1:
        return None
    middel_index = len(array)//2
    left_array = array[:middel_index]
    right_array = array[middel_index:]
    merge_sort(left_array)
    merge_sort(right_array)
    i = 0                  # left sub array index
    j = 0                  # right sub array index
    k = 0                  # merged array index
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        array[k] = right_array[j]
        j +=1
        k += 1
