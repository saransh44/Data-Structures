def max (lst, index):
    print('c')
    m = 0
    if not lst:
       return None
    if (index == len(lst) -1):
        if (lst[index] > lst[index-1]):
            return lst[index]
            print('a')
        else:
            return lst[index-1]
            print('b')
    else:
        # for i in range(len(lst)):
        #     if(lst[index] < lst[i]):
        #         index = i
        if (lst[index] > lst[index+1]):
            m = lst[index]
        else:
            m = lst[index+1]

        if (m > max(lst,index+1)):
            return m
        else:
            return max(lst, index + 1)


        # else:
        #     return lst[index]
        # max(lst, index+1)


print(max([1,2,100,4,5,12,2],0))


