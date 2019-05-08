# class Solution(object):
#     def __init__(self):
#         self.memo = []
#     def integerBreak(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2
#
#         self.memo = [0] * (n+1)
#         return self.calc(n)
#
#     def calc(self, n):
#         self.memo[2] = 2
#         self.memo[3] = 3
#         res = 0
#         for i in range(1, n):
#             if self.memo[i] == 0:
#                 res = (n-i) * self.calc(i)
#
#             else:
#                 res = (n-i) * self.memo[i]
#             if res > self.memo[n]:
#                 self.memo[n] = res
#         return self.memo[n]

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        memo = [-1] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                memo[i] = max(memo[i], max(j*(i-j), j*memo[i-j]))
        return memo[n]

if __name__ == '__main__':
    n = 10
    print(Solution().integerBreak(n))
