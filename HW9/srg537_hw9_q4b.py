def intersection_list(lst1, lst2):

    dict = {}

    result = []

    for i in range(len(lst2)):
        dict[lst2[i]] = 1

    # print(dict)

    for i in range(len(lst1)):
        if dict.get(lst1[i]) is not None:
            result.append(lst1[i])

    return result

print(intersection_list([3, 9, 2, 7, 1], [4, 1, 8, 2]))
