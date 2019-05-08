def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    new_nums = sorted(nums)
    i = 0
    j = len(nums) - 1
    ans = []
    res = {}
    for m in range(len(nums)):
        if nums[m] not in res:
            res[nums[m]] = [m]
        else:
            res[nums[m]].append(m)
    while i < j:
        if new_nums[i] + new_nums[j] == target:
            if new_nums[i] != new_nums[j]:
                x, y = res[new_nums[i]][0], res[new_nums[j]][0]
                ans = [x,y]
            else:
                x, y = res[new_nums[i]][0], res[new_nums[i]][1]
                ans = [x,y]
            break
        elif new_nums[i] + new_nums[j] > target:
            j -= 1
        else:
            i += 1
    return ans

    # res = {}
    # ans = []
    # for i in nums:
    #     if i not in res:
    #         res[i] = 1
    #     else:
    #         res[i] += 1
    # for i in range(len(nums)):
    #     num = target - nums[i]
    #     if num != nums[i] and num in res:
    #         j = nums.index(num)
    #         ans = [i, j]
    #         break
    #     if num == nums[i] and res[num] >= 2:
    #         nums.remove(nums[i])
    #         j = nums.index(num) + 1
    #         ans = [i, j]
    #         break
    # return ans

    res = {}
    ans = []
    for i in range(len(nums)):
        num = target - nums[i]
        if num in res:
            ans = [i, res[num]]
            return ans
        res[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
