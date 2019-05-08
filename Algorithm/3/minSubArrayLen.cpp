#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int l = 0, r = -1; // nums[l...r]Ϊ���ǵĻ�������
        int sum = 0;
        int res = nums.size() + 1;

        while(l < nums.size()) {
            if (r + 1 < nums.size() && sum < s)
                sum += nums[++r];
            else
                sum -= nums[l++];

            if(sum >= s)
                res = min(res, r-l+1);
            }

        if(res == nums.size() + 1)
            return 0;
        return res;
    }
};

int main() {
    int arr[] = {2, 3, 1, 2, 4, 3};
    vector<int> vec(arr, arr + sizeof(arr)/sizeof(int));
    int s = 7;
    int res = Solution().minSubArrayLen(s,vec);
    cout << res << endl;
    return 0;
}
