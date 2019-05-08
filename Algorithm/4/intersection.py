def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1 = set(nums1)
    nums2 = set(nums2)
    res = []
    if not nums1 or not nums2:
        return []
    for i in nums1:
        if i in nums2:
            res.append(i)
    return res

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersection(nums1, nums2))
