def move_zeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            del nums[i:i+1]
            nums.append(0)


list = [0,1,3, 0, 5, 0, 432, 4]
move_zeros(list)

print(list)

