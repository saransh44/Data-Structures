# Question2A and 2B
def shift (lst, k, dir = "left"):
    if (dir == "left"):
        print("left scenerio")
        for n in range(k):
            lst.append(lst[n])
        del lst[0:k]
    else:
        a = 0
        print("right scenerio")
        b = len(lst) - 1
        for n in range(k):
            lst.insert(n,lst[b])
        del lst[len(lst)-k:]
        # for n in range(k):
        #     lst.pop([len(lst)-1])
        # del lst[len[lst]-1-k:]


lst2 = [1, 2, 3, 4, 5, 6]
print (lst2)
shift (lst2, 4, "right")
print (lst2)




# def shift (lst, k):
#     for i in range(k):
#         print(i)
#         lst.pop(i)

# def shift (lst, k):
#     for n in range(k):
#         lst.append(lst[n])
#     del lst[0:k]

# lst2 = [1, 2, 3, 4, 5, 6]
# print (lst2)
# shift (lst2, 4)
# print (lst2)