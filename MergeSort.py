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

    #Initialize a list
    merged_size = k - i + 1
    merged_L = []
    for a in range(merged_size):
        merged_L.append(0)

    merge_pos = 0
    left = i
    right = j + 1

    while left <= j and right <= k:
        if L[left] < L[right]:
            merged_L[merge_pos] = L[left]
            left += 1
        else:
            merged_L[merge_pos] = L[right]
            right += 1
        merge_pos += 1

    while left <= j:
        merged_L[merge_pos] = L[left]
        left += 1
        merge_pos += 1

    while right <= k:
        merged_L[merge_pos] = L[right]
        right += 1
        merge_pos += 1

    for a in range(merged_size):
        L[i + a] = merged_L[a]


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

UnsortedList = []
for a in range(9):
    x = randrange(99)
    UnsortedList.append(x)

KeyList = sorted(UnsortedList)
print(KeyList)

MergeSort(UnsortedList, 0, len(UnsortedList)-1)
print(UnsortedList)