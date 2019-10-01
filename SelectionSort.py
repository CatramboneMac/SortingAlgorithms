from random import randrange

def SelectionSort(L):
    """
    Sorts a given list by repeatedly finding the minimum value in the list
    and swapping it with the value at the current index
    :param L: Unsorted list
    :return: None
    """
    for i in range(len(L)-1):  # Iterates thru the indices of the list
        min = i  # Assumes the minimum value to be at index i
        for j in range(i+1, len(L)):  # Searches thru the rest of the list
            if L[j] < L[min]:  # If we find a value lower than the minimum
                min = j  # Update the minimum to be at index j
        L[i], L[min] = L[min], L[i]  # Swaps the minimum value and the value at the current index


unsorted_list = []
for a in range(9):
    x = randrange(99)
    unsorted_list.append(x)

key = sorted(unsorted_list)
print(key)

SelectionSort(unsorted_list)
print(unsorted_list)
