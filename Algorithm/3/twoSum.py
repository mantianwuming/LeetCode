def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # for i in range(len(numbers)):
    #     new_t = target - numbers[i]
    #     newnums = numbers[i+1:]
    #     l, r = 0, len(newnums)-1
    #     while l <= r:
    #         mid = int(l + (r-l)/2)
    #         if new_t == newnums[mid]:
    #             return [i+1, mid+i+2]
    #         elif new_t > newnums[mid]:
    #             l = mid + 1
    #         elif new_t < newnums[mid]:
    #             r = mid - 1

    i, j = 0, len(numbers) - 1
    while (i < j):
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        if numbers[i] + numbers[j] < target:
            i += 1
        if numbers[i] + numbers[j] > target:
            j -= 1

nums = [2,7, 11, 15]
target = 9
print(twoSum(nums,target))
