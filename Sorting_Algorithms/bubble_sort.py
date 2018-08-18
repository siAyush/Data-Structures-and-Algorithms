'''
Bubble Sort -->
Bubble Sort is a comparison based sorting algorithm.It compares each pair of
adjacent items and swap them if  they are in the wrong order.It is in-place and
stable sorting algorithm and no need of extra memory for sorting.
Time Complexity --- O(N^2)
'''
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
