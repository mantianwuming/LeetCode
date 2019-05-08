def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = {}
    ans = []
    for i in range(len(nums)):
        if nums[i] in res:
            res[nums[i]] += 1
        else:
            res[nums[i]] = 1
    t = sorted(res.items(), key=lambda l : l[1] ,reverse=True)
    for i in range(k):
        ans.append(t[i][0])

    return ans

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))
