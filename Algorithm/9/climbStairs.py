class Solution(object):
    def __init__(self):
        self.memo = []
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = [-1] * (n+1)
        return self.calcWays(n)

    def calcWays(self,n):
        if n == 0 or n == 1:
            return 1
        if self.memo[n] == -1:
            self.memo[n] = self.calcWays(n-1) + self.calcWays(n-2)
        return self.memo[n]

# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         a = 1
#         b = 2
#         res = 0
#         for i in range(3, n+1):
#             res = a + b
#             a = b
#             b = res
#         return res
