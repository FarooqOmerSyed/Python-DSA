def bubble(list1):
    indexing_length = len(list1) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, indexing_length):
            if list1[i] > list1[i + 1]:
                is_sorted = False
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

    return list1


print(bubble([4, 3, 1, 2]))
