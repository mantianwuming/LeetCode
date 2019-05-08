def containsNearbyAlmostDuplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    res = set()
    for i in range(len(nums)):
        if t == 0:
            if nums[i] in res:
                return True
        else:
            for num in res:
                if abs(nums[i] - num) <= t:
                    return True
        res.add(nums[i])
        if len(res) == k+1:
            res.remove(nums[i-k])
    return False

    # res = set()
    # for i in range(len(nums)):
    #     for num in res:
    #         if abs(nums[i] - num) <= t:
    #             return True
    #     res.add(nums[i])
    #     if len(res) == k + 1:
    #         res.remove(nums[i - k])
    # return False

nums = [1,2,3,1]
k = 3
t = 0
print(containsNearbyAlmostDuplicate(nums, k ,t))
