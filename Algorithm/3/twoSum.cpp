#include <iostream>
#include <vector>
#include <cassert>
#include <stdexcept>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // for(int i = 0; i < numbers.size(); i++){
        //     int new_t = target - numbers[i];
        //     vector<int> newnums;
        //     for(int j = 0; j < numbers.size() - i - 1; j++)
        //         newnums[j] = numbers[i+j+1];
        //     int l = 0, r = newnums.size() - 1;
        //     while(l<=r){
        //         int mid = l + (r-l) / 2;
        //         if(new_t == newnums[mid]){
        //             int res[2] = {i+1, mid + i + 2};
        //             return vector<int>(res, res+2);
        //             }
        //         if(new_t > newnums[mid])
        //             l = mid + 1;
        //         if(new_t < newnums[mid])
        //             r = mid - 1;
        //     }
        // }

        assert(numbers.size() >= 2);
        int l = 0, r = numbers.size() - 1;
        while(l < r) {
          if(numbers[l] + numbers[r] == target){
            int res[2] = {l+1, r+1};
            return vector<int>(res, res+2);
          }
          else if(numbers[l] + numbers[r] < target)
            l++;
          else
            r--;
        }

        throw invalid_argument("The input has no solution.");
    }
};

int main() {
  int arr[] = {2, 7, 11, 15};
  int target = 9;
  vector<int> vec(arr, arr + sizeof(arr)/sizeof(int));
  vector<int> res = Solution().twoSum(vec, target);
  for(int i = 0; i < res.size(); i++)
    cout << res[i] << " ";
  cout << endl;
  return 0;
}
