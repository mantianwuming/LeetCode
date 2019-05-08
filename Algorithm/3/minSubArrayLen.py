def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    # for i in range(len(nums)):
    #     if nums[i] >= s:
    #         return 1
    # minsize = len(nums) + 1
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         nums_sub = nums[i:j+1]
    #         if sum(nums_sub) >= s:
    #             if j - i + 1 < minsize:
    #                 minsize = j-i+1
    # if minsize > len(nums):
    #         minsize = 0
    # return minsize

    # for i in range(len(nums)):
    #     if nums[i] >= s:
    #         return 1
    # i, j = 0, 1
    # minsize = len(nums) + 1
    # while(j<len(nums)):
    #     if sum(nums[i:j+1]) >= s:
    #         if j - i + 1 < minsize:
    #             minsize = j - i + 1
    #         i += 1
    #     if sum(nums[i:j+1]) < s:
    #         j += 1
    # if minsize > len(nums):
    #     return 0
    # return minsize

    l, r = 0, -1
    sum = 0
    res = len(nums) + 1
    while(l < len(nums)):
        if(r + 1 < len(nums) and sum < s):
            r += 1
            sum += nums[r]
        else:
            sum -= nums[l]
            l += 1

        if sum >= s:
            res = min(res, r-l+1)

    if res == len(nums) + 1:
        return 0
    return res

nums = [2,3,1,2,4,3]
print(minSubArrayLen(7,nums))
