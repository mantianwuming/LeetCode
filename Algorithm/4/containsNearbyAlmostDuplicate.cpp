#include <iostream>
#include <vector>
#include <set>
#include <math>

using namespace std;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {

        set<long long> record;
        for(int i = 0;i <nums.size(); i++){
            if(record.lower_bound( (long long)nums[i] - (long long)t) != record.end() && *record.lower_bound((long long)nums[i] - (long long)t) <= (long long)nums[i] + (long long)t)
                return true;
            record.insert(nums[i]);

            //保持record中最多有k个元素
            if(record.size() == k + 1)
                record.erase(nums[i-k]);
        }
        return false;
    }
};

int main(){

    return 0;
}
