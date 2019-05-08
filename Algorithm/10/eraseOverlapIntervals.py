class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals)
        memo = [1 for i in range(len(intervals))]

        for i in range(1, len(intervals)):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    memo[i] = max(memo[i], 1 + memo[j])
        return len(intervals) - max(memo)

import functools
class Solution1(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        # intervals = sorted(intervals,key=functools.cmp_to_key(compare))
        intervals = sorted(intervals, key = lambda x:x[1])

        res = 1;
        pre = 0;
        for i in range(1, len(intervals)):
            if(intervals[i][0] >= intervals[pre][1]):
                res += 1
                pre = i
        return len(intervals) - res


def compare(x,y):
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]:
        return -1
    elif x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    intervals = [ [1,2], [2,3], [3,4], [1,3] ]
    print(Solution1().eraseOverlapIntervals(intervals))
