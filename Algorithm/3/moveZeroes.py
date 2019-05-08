class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # zeros = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         zeros += 1
        # for i in range(n-zeros):
        #     if nums[i] == 0:
        #         nums = (nums[:i] + nums[i+1:])
        #         nums.append(0)
        #
        # return nums

        # n = len(nums)
        # newlist = []
        # for i in range(n):
        #     if nums[i] != 0:
        #         newlist.append(nums[i])
        # for i in range(len(newlist)):
        #     nums[i] = newlist[i]
        # for i in range(len(newlist), n):
        #     nums[i] = 0

        # n = nums.count(0)
        # for i in range(n):
        #     nums.remove(0)
        #     nums.append(0)

        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j += 1

        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0

        return nums





if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    nums = sol.moveZeroes(nums)
    print(nums)
