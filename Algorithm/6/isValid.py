class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for i in s:
            if i in left:
                res.append(i)
            if i in right:
                if not res:
                    return False
                else:
                    m = res.pop()
                    if left.index(m) != right.index(i):
                        return False
        if not res:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    s = '('
    print(sol.isValid(s))
