class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        while g and s:
            maxs = s[0]
            maxg = g[0]
            if maxs >= maxg:
                res += 1
                s.pop(0)
                g.pop(0)
            else:
                g.pop(0)
        return res

class Solution1(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g = sorted(g)
        s = sorted(s)
        while g and s:
            maxs = s[-1]
            maxg = g[-1]
            if maxs >= maxg:
                res += 1
                s.pop()
                g.pop()
            else:
                g.pop()
        return res

class Solution2(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        si, gi = 0, 0
        while gi < len(g) and si < len(s):
            if  s[si] >= g[gi]:
                res += 1
                si += 1
                gi += 1
            else:
                gi += 1
        return res

if __name__ == '__main__':
    g = [1,2,3]
    s = [1,1]
    print(Solution2().findContentChildren(g,s))
