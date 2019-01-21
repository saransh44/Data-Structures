def split_parity (lst):
    left = 0
    right  = (len(lst) - 1)

    while (left < right):

        if (lst[left] % 2 == 0 and lst[right] % 2 == 1):
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
            left += 1

        if (lst[left] % 2 == 0 and lst[right] % 2 == 0):
            # if left is even
            print("right")
            # lst.append(lst[left])
            right -= 1

        if (lst[left] % 2 == 1 and lst[right] % 2 == 1):
            left += 1

        if (lst[left] % 2 == 1 and lst[right] % 2 == 0):
            right -= 1
            left += 1

    # lst.reverse()
    return lst

print(split_parity([7,4,10,5,6,23,8,2]))