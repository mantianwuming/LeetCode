class Solution(object):
    def __init__(self):
        self.memo = []

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        addsum = sum(nums);
        if addsum % 2 != 0:
            return False
        self.memo = [[-1 for i in range(addsum//2 + 1)] for i in range(len(nums))]
        return self.tryPartition(nums, len(nums)-1, addsum//2)

    def tryPartition(self, nums, index, addsum):
        if addsum == 0:
            return True

        if addsum < 0 or index < 0:
            return False

        if self.memo[index][addsum] != -1:
            return self.memo[index][addsum]

        if self.tryPartition(nums, index - 1, addsum) or self.tryPartition(nums, index - 1, addsum-nums[index]):
            self.memo[index][addsum] = 1
        else:
            self.memo[index][addsum] = 0

        return self.memo[index][addsum] == 1

class Solution1(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        addsum = sum(nums);
        if addsum % 2 != 0:
            return False
        n = len(nums)
        C = addsum//2
        memo = [False for i in range(C+1)]
        for i in range(C+1):
            memo[i] = (nums[0] == i)

        for i in range(1,n):
            for j in range(C, nums[i]-1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]

        return memo[C]


if __name__ == '__main__':
    nums = [1,5,11,5]
    print(Solution1().canPartition(nums))
