class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            result = self.permute(nums[0:i]+ nums[i+1:])
            for j in result:
                j.append(nums[i])
                res.append(j)
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))
