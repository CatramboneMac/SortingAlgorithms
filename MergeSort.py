from random import randrange

def Merge(L, i, j, k):
    """
    Sorts a portion of a given list
    by comparing elements in two specified partitions
    :param L: Unsorted list
    :param i: first index of the left partition
    :param j: last index of the left partition
    :param k: last index of the right partition
    :return: None
    """

    # Initialize merged_list to be the size of both partitions combined
    merged_size = k - i + 1
    merged_list = []  # Start with an empty list
    for a in range(merged_size):
        merged_list.append(0)  # Fill the list with zeros (for now)

    merge_pos = 0
    left = i  # First index of the left partition
    right = j + 1  # First index of the right partition

    # Compares two elements, one from each partition
    # Adds the smaller of the two to merged_list
    while left <= j and right <= k:  # Ensuring we are within the bounds of the left and right partitions
        if L[left] < L[right]:
            merged_list[merge_pos] = L[left]
            left += 1  # Increment index of the left partition
        else:
            merged_list[merge_pos] = L[right]
            right += 1  # Increment index of the right partition
        merge_pos += 1  # Increment merge_pos to the next index

    # If left partition is not empty
    # Add the rest of the left partition to merged_list
    while left <= j:
        merged_list[merge_pos] = L[left]
        left += 1
        merge_pos += 1

    # If right partition is not empty
    # Add the rest of the right partition to merged_list
    while right <= k:
        merged_list[merge_pos] = L[right]
        right += 1
        merge_pos += 1

    # At this point, merged_list will contain
    # every value from the left and right partitions
    # and will be sorted in ascending order

    # Replaces L[i:k] with merged_list[:]
    for a in range(merged_size):
        L[i + a] = merged_list[a]


def MergeSort(L, i, k):
    """
    Sorts a given list by
    recursively partitioning the list into two halves,
    then merging partitions together using the Merge function
    :param L: Unsorted list
    :param i: first index of the partition
    :param k: last index of the partition
    :return: None
    """

    if i < k:
        j = (i + k) // 2
        MergeSort(L, i, j)
        MergeSort(L, j+1, k)

        Merge(L, i, j, k)


unsorted_list = []
for a in range(9):
    x = randrange(99)
    unsorted_list.append(x)

key = sorted(unsorted_list)
print(key)

MergeSort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)