def intersection_list(lst1, lst2):
    lst1.sort()
    lst2.sort()

    i = 0
    i2 = 0

    result = []
    while i < len(lst1) and i2 < len(lst2):
        if lst1[i] == lst2[i2]:
            result.append(lst1[i])
            i += 1
            i2 += 1

        elif lst1[i] < lst2[i2]:
            i += 1
        else:
            i2 += 1

    return result

# print(intersection_list([4, 9, 2, 7, 1], [4, 1, 8]))


