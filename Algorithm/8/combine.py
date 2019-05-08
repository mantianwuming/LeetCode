class Solution(object):
    def __init__(self):
        self.res = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 or k <= 0 or k > n:
            return []
        c = []
        self.generateCombination(n,k,1,c)
        return self.res


    def generateCombination(self, n, k, start, c):
        if len(c) == k:
            self.res.append(c.copy())
            return
        for i in range(start, n+1):
            c.append(i)
            self.generateCombination(n,k,i+1, c)
            c.pop()
        return

if __name__ == "__main__":
    n = 4
    k = 2
    res = Solution().combine(4,2)
    print(res)
