'''
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and
partitions the given array around the picked pivot.It is not a stable algorithm
(don't preserve the order of equal items).
'''
def quick_sort(array,low,high):
    if low >= high:
        return None
    pivot = partition(array,low,high)
    quick_sort(array,low,pivot-1)
    quick_sort(array,pivot+1,high)

def partition(array,low,high):
    pivot_index = low+high//2
    array[pivot_index],array[high] = array[high],array[pivot_index]   # swaping
    initial = low
    for i in range(low,high):
        if array[i] <= array[high]:
            array[i],array[initial] = array[initial],array[i]        # swaping
            initial += 1
    array[initial],array[high] = array[high],array[initial]          # swaping
    return initial
