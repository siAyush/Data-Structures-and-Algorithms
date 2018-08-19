'''
Selection Sort is a O(N^2) complexity algorithm.
This algorithm proceeds by finding the smallest item in the
unsorted array.And then swap it with the leftmost unsorted
element.It doesn't need extra memory for sortingself.
'''

def selection_sort(array):
    for i in range(len(array)-1):
        index = i
        for j in range(i+1,len(array)):
            if array[j] < array[index]:
                index = j
        if index != i:
            array[index],array[i] = array[i],array[index]
    return array
