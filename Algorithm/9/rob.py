# # out of time
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0;
#         if len(nums) == 2 or len(nums) == 1:
#             return max(nums)
#         if len(nums) == 3:
#             return max(nums[0] + nums[2], nums[1])
#         a = nums[0] + self.rob(nums[2:])
#         b = nums[1] + self.rob(nums[3:])
#         return max(a, b)

# class Solution(object):
#     def __init__(self):
#         self.memo = []
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         self.memo = [-1] * len(nums)
#         return self.tryRob(nums, 0)
#
#     def tryRob(self, nums, index):
#         if index >= len(nums):
#             return 0
#         if(self.memo[index] != -1):
#             return self.memo[index]
#         res = 0
#         for i in range(index, len(nums)):
#             res = max(res, nums[i] + self.tryRob(nums, i+2))
#         self.memo[index] = res
#         return res

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        memo = [-1] * n
        memo[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                if j + 2 >= n:
                    memo[i] = max(memo[i], nums[j])
                else:
                    memo[i] = max(memo[i], nums[j] + memo[j+2])
        return memo[0]

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().rob(nums))
