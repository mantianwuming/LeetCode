import numpy as np

class Solution(object):
    def __init__(self):
        self.visited = list()
        self.d = [[-1,0], [0,1], [1,0], [0,-1]]
        self.m = 0
        self.n = 0

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m = len(board)
        self.n = len(board[0])
        self.visited = np.zeros((self.m,self.n))
        for i in range(self.m):
            for j in range(self.n):
                if self.searchWord(board, word, 0, i, j):
                    return True
        return False

    def searchWord(self, board, word, index, startx, starty):
        if index == len(word) - 1:
            return board[startx][starty] == word[index]
        if board[startx][starty] == word[index]:
            self.visited[startx][starty] = 1
            for i in range(4):
                newx = startx + self.d[i][0]
                newy = starty + self.d[i][1]
                if(self.inArea(newx, newy) and self.visited[newx][newy] != 1 and self.searchWord(board, word, index+1, newx, newy)):
                    return True;
            self.visited[startx][starty] = 0
        return False

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

if __name__ == "__main__":
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = 'ABCCED'
    print(Solution().exist(board, word))
