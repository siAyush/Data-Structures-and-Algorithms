
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array


a = [i for i in reversed(range(500))]
bubble_sort(a)
print(a)
