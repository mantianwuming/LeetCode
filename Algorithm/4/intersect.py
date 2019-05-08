def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)
    return res

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = {}
    ans = []
    for i in nums1:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    for i in nums2:
        if i in res and res[i] > 0:
            ans.append(i)
            res[i] -= 1
    return ans
