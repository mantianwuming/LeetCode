class Solution(object):
    def __init__(self):
        self.memo = []

    def knapsack01(self,w, v, C):
        n = len(w)
        self.memo = [[-1 for i in range(C+1)] for i in range(n)]
        return self.bestValue(w, v, n-1, C);

    def bestValue(self, w, v, index, c):
        if index < 0 or c <= 0:
            return 0
        if self.memo[index][c] != -1:
            return self.memo[index][c]

        res = self.bestValue(w,v,index-1,c)
        if c >= w[index]:
            res = max(res, v[index] + self.bestValue(w, v, index-1, c-w[index]))
        self.memo[index][c] = res;
        return res;

class Solution1(object):
    def knapsack01(self,w,v,C):
        n = len(w)
        if n == 0:
            return 0

        memo = [[-1 for i in range(C+1)] for i in range(n)]

        for j in range(C+1):
            if j >= w[0]:
                memo[0][j] = v[0]
            else:
                memo[0][j] = 0


        for i in range(1,n):
            for j in range(C+1):
                memo[i][j] = memo[i-1][j]
                if j >= w[i]:
                    memo[i][j] = max(memo[i][j], v[i] + memo[i-1][j-w[i]])

        return memo[n-1][C]

class Solution2(object):
    def knapsack01(self,w,v,C):
        n = len(w)
        if n == 0:
            return 0

        memo = [[-1 for i in range(C+1)] for i in range(2)]

        for j in range(C+1):
            if j >= w[0]:
                memo[0][j] = v[0]
            else:
                memo[0][j] = 0

        for i in range(1,n):
            for j in range(C+1):
                memo[i%2][j] = memo[(i-1)%2][j]
                if j >= w[i]:
                    memo[i%2][j] = max(memo[i%2][j], v[i] + memo[(i-1)%2][j-w[i]])

        return memo[(n-1)%2][C]

class Solution3(object):
    def knapsack01(self,w,v,C):
        n = len(w)
        if n == 0:
            return 0

        memo = [-1 for i in range(C+1)]

        for j in range(C+1):
            if j >= w[0]:
                memo[j] = v[0]
            else:
                memo[j] = 0

        for i in range(1,n):
            for j in range(C, w[i]-1, -1):
                memo[j] = max(memo[j], v[i] + memo[j-w[i]])

        return memo[C]
if __name__ == '__main__':
    w = [1,2,3]
    v = [6,10,12]
    C = 5
    print(Solution1().knapsack01(w,v,C))
