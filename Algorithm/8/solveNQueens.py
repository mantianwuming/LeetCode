import numpy as np

class Solution(object):
    def __init__(self):
        self.res = list()
        self.col = list()
        self.dia1 = list()
        self.dia2 = list()
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.col = np.zeros(n)
        self.dia1 = np.zeros(2*n-1)
        self.dia2 = np.zeros(2*n-1)
        row = list()
        self.putQueen(n, 0, row)
        return self.res

    def putQueen(self, n, index, row):
        if index == n:
            self.res.append(self.generateBoard(n, row))
            return
        for i in range(n):
            if self.col[i] != 1 and self.dia1[index + i] != 1 and self.dia2[index - i + n - 1] != 1:
                row.append(i)
                self.col[i] = 1
                self.dia1[index + i] = 1
                self.dia2[index - i + n - 1] = 1
                self.putQueen(n, index+1, row)
                self.col[i] = 0
                self.dia1[index + i] = 0
                self.dia2[index - i + n - 1] = 0
                row.pop()
        return

    def generateBoard(self, n, row):
        x = '.' * n
        board = list()
        for i in range(n):
            board.append(x)
        for i in range(n):
            a = list(board[i])
            a[row[i]] = 'Q'
            board[i] = ''.join(a)
        return board

if __name__ == '__main__':
    n = 4
    res = Solution().solveNQueens(n)
    for i in range(len(res)):
        for j in range(n):
            print(res[i][j], '\n')
        print('\n')
