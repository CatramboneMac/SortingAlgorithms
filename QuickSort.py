from random import randrange

def Partition(L, i, k):
    """
    Separates the data into two unsorted partitions
    a low partition (i - high) containing values lower than or equal to a selected pivot
            and
    a high partition (high - k) containing values greater than or equal to a selected pivot
    :param L: Unsorted list
    :param i: Starting index of the range we want to partition
    :param k: Ending index of the range we want to partition
    :return: high - the highest index of the low partition
    """

    midpoint = (i + k) // 2  # Use the lower and upper bound to determine the midpoint
    pivot = L[midpoint]  # The pivot will be the value of the middle element

    low = i
    high = k

    # Loop until we are properly partitioned
    done = False
    while not done:
        # Incremented low until a value greater than the pivot is found
        while L[low] < pivot:
            low += 1
        # Decrement low until a value less than the pivot is found
        while L[high] > pivot:
            high -= 1

        if low >= high:  # If low is greater than or equal to high:
            done = True  # The data is properly partitioned
        else:
            L[low], L[high] = L[high], L[low]  # Swap the values at the low and high index
            low += 1  # Increment low
            high -= 1  # Decrement high
    return high  # Return the highest index of the low partition


def QuickSort(L, i, k):
    """
    Sorts a give list (L) by recursively partitioning it using the Partition() function
    :param L: Unsorted list
    :param i: Lower bound of the data we want sorted (typically i = 0)
    :param k: Upper bound of the data we want sorted (typically k = len(L) - 1 )
    :return: None
    """
    # Base case:
    if i >= k:
        return
    else:
        j = Partition(L, i, k)
        QuickSort(L, i, j)
        QuickSort(L, j + 1, k)


unsorted_list = []
for a in range(9):
    x = randrange(99)
    unsorted_list.append(x)

key = sorted(unsorted_list)
print(key)

QuickSort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)