#include <iostream>
#include <vector>

using namespace std;

// // Definition for an interval.
// struct Interval{
//     int start;
//     int end;
//     Interval() : start(0), end(0) {}
//     Interval(int s, int e) : start(s), end(e) {}
// };
//
// bool compare(const Interval &a, const Interval &b){
//     if(a.start != b.start)
//         return a.start < b.start;
//     return a.end < b.end;
// }
//
// class Solution {
// public:
//     int eraseOverlapIntervals(vector<Interval>& intervals){
//         if(intervals.size() == 0)
//             return 0;
//         sort(intervals.begin(), intervals.end(), compare);
//
//         // memo[i] 表示使用intervals[0...i]的区间能构成的最长不重叠区间序列
//         vector<int> memo(intervals.size(), 1);
//         for(int i = 1; i < intervals.size(); i++)
//             // memo[i]
//             for(int j = 0; j < i; j++)
//                 if(intervals[i].start >= intervals[j].end)
//                     memo[i] = max(memo[i], 1 + memo[j]);
//         int res = 0;
//         for(int i = 0; i < memo.size(); i++)
//             res = max(res, memo[i]);
//         return intervals.size() - res;
//     }
// };

bool compare(vector<int> &a, vector<int> &b){
    if(a[0] != b[0])
        return a[0] < b[0];
    else return a[1] < b[1];
}

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size() == 0)
            return 0;
        sort(intervals.begin(), intervals.end(), compare);

        vector<int> memo(intervals.size(), 1);
        for(int i = 1; i < intervals.size(); i++)
            for(int j = 0; j < i; j++)
                if(intervals[i][0] >= intervals[j][1])
                    memo[i] = max(memo[i], 1 + memo[j]);
        int res = 0;
        for(int i = 0; i < memo.size(); i++)
            res = max(res, memo[i]);
        return intervals.size() - res;
    }
};

bool compare1(vector<int> &a, vector<int> &b){
    if(a[1] != b[1])
        return a[1] < b[1];
    else return a[0] < b[0];
}

class Solution1 {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.size() == 0)
            return 0;
        sort(intervals.begin(), intervals.end(), compare1);

        int res = 1;
        int pre = 0;
        for(int i = 1; i < intervals.size(); i++)
            if(intervals[i][0] >= intervals[pre][1]){
                res++;
                pre = i;
            }
        return intervals.size() - res;
    }
};

int main(){

    return 0;
}
