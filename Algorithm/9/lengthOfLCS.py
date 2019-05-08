class Solution(object):
    def lengthOfLCS(self, s1, s2):
        m = len(s1)
        n = len(s2)
        if m == 0 or n == 0:
            return 0

        memo = [[0 for i in range(n)] for i in range(m)]

        for i in range(n):
            if s1[0] == s2[i]:
                memo[0][i] = 1
                for x in range(i, n):
                    memo[0][x] = 1
        for j in range(m):
            if s1[j] == s2[0]:
                memo[j][0] = 1
                for x in range(j, m):
                    memo[x][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                if s1[i] == s2[j]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])

        return memo[m-1][n-1]

if __name__ == '__main__':
    s1 = 'XAXBCD'
    s2 = 'AXCED'
    print(Solution().lengthOfLCS(s1,s2))
