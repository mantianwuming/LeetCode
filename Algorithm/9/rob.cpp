#include <iostream>
#include <vector>

using namespace std;

// class Solution {
// private:
//     // memo[i]表示考虑寻找nums[i...n)所能获得的最大收益
//     vector<int> memo;
//     // 考虑寻找 nums[index...nums.size())这个范围的所有房子
//     int tryRob(vector<int>& nums, int index){
//         if(index >= nums.size())
//             return 0;
//         if(memo[index] != -1)
//             return memo[index];
//         int res = 0;
//         for(int i = index; i < nums.size(); i++)
//             res = max(res, nums[i] + tryRob(nums, i+2));
//         memo[index] = res;
//         return res;
//     }
// public:
//     int rob(vector<int>& nums) {
//         memo = vector<int>(nums.size(), -1);
//         return tryRob(nums, 0);
//     }
// };


class Solution {
public:
    int rob(vector<int>& nums) {

        int n = nums.size();
        if(n == 0)
            return 0;
        // memo[i]表示考虑寻找nums[i...n-1]所能获得的最大收益
        vector<int> memo(n, -1);
        memo[n-1] = nums[n-1];
        for(int i = n-2; i >= 0; i--)
            // memo[i]
            for(int j = i; j < n; j++)
                memo[i] = max(memo[i], nums[j] + (j + 2 < n ? memo[j+2] : 0));
        return memo[0];
    }
};


int main(){
    vector<int> nums = {4,3,1,2};
    cout << Solution().rob(nums) << endl;
    return 0;
}
