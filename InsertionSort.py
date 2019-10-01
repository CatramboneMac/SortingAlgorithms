from random import randrange

def InsertionSort(L):
    for i in range(1, len(L)):
        j = i-1
        key = L[i]
        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key
    return L


unsorted_list = []
for a in range(9):
    x = randrange(99)
    unsorted_list.append(x)

key = sorted(unsorted_list)
print(key)

SortedList = InsertionSort(unsorted_list)
print(unsorted_list)