def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # for i in range(len(nums)):
    #     j = i + 1
    #     while j - i <= k and j < len(nums):
    #         if nums[i] == nums[j]:
    #             return True
    #         j += 1

    res = set()
    for i in range(len(nums)):
        if nums[i] in res:
            return True
        res.add(nums[i])
        if len(res) == k+1:
            res.remove(nums[i-k])
    return False

    # 
    # res = {}
    # for i in range(len(nums)):
    #     if nums[i] in res:
    #         if -k <= i - res[nums[i]] <= k:
    #             return True
    #         else:
    #             res[nums[i]] = i
    #     res[nums[i]] = i
    # return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))
