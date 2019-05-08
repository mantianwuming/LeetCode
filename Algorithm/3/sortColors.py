def sortColors(nums):
    # x = [0,0,0]
    # for i in range(len(nums)):
    #     assert (nums[i]>=0 and nums[i] <= 2)
    #     x[nums[i]] += 1
    # for i in range(x[0]):
    #     nums[i] = 0
    # for i in range(x[0], x[0] + x[1]):
    #     nums[i] = 1
    # for i in range(x[0] + x[1], x[0] + x[1] + x[2]):
    #     nums[i] = 2

    # index = 0
    # for i in range(3):
    #     for j in range(x[i]):
    #         nums[index] = i
    #         index += 1
    zero = -1
    two = len(nums)
    i = 0
    while(i < two):
        if nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            two -= 1
            nums[i], nums[two] = nums[two], nums[i]
        else:
            assert(nums[i] == 0)
            zero += 1
            nums[zero], nums[i] = nums[i], nums[zero]
            i += 1
    return nums

nums = [0,1,2,0,1,1,2]
print(sortColors(nums))
