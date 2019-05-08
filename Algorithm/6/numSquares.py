import numpy as np
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [[n,0]]
        visited = np.zeros(n+1)
        visited[n] = 1
        while q:
            temp = q.pop(0)
            num = temp[0]
            step = temp[1]
            for i in range(1,n+1):
                a = num - i*i
                if a < 0:
                    break
                if a == 0:
                    return step + 1
                if not visited[a]:
                    q.append([a, step+1])
                    visited[a] = 1

if __name__ == "__main__":
    sol = Solution()
    n = 1
    print(sol.numSquares(n))
