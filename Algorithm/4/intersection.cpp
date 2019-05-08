#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

        // unordered_set<int> record;
        set<int> record;
        for(int i =0; i < nums1.size(); i++)
            record.insert(nums1[i]);
        // set<int> record(nums1.begin(), nums1.end());

        // unordered_set<int> resultSet;
        set<int> resultSet;
        for(int i = 0; i < nums2.size(); i++)
            if(record.find(nums2[i]) != record.end())
                resultSet.insert(nums2[i]);

        // vector<int> resultVector;
        // for(set<int>::iterator iter = resultSet.begin(); iter != resultSet.end(); iter++)
        //     resultVector.push_back(*iter);
        // return resultVector;
        return vector<int>(resultSet.begin(), resultSet.end());
    }
};

int main(){

    return 0;
}
