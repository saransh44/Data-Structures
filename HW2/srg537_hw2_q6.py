def two_sum(srt_lst, target):
    left = 0
    right = (len(srt_lst) - 1)

    while (left < right):
        if (srt_lst[left] + srt_lst[right] > target):
            right -= 1
        elif (srt_lst[right] + srt_lst[left] < target):
            left += 1
        elif (srt_lst[right] + srt_lst[left] == target):
            return (left, right)
        else:
            return None

    # print(srt_lst)
    # initial = srt_lst[0]
    # for element in srt_lst:
    #     if(initial + element == target):
    #         return srt_lst.index(element), str_
    #
    # # del srt_lst[0:1]
    #
    # return 1+ two_sum(srt_lst[1:], target)

print(two_sum([-2, 6, 7, 11, 12, 21], 22))
