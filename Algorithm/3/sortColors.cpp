#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
      // int count[3] = {0};
      // for (int i = 0; i < nums.size(); i++){
      //   assert(nums[i] >= 0 && nums[i] <= 2);
      //   count[nums[i]]++;
      // }
      // int index = 0;
      //
      // for(int j = 0; j < 3; j++){
      //   for(int i = 0; i < count[j]; i++)
      //     nums[index++] = j;
      // }

      // for(int i = 0; i < count[0]; i++)
      //   nums[index++] = 0;
      // for(int i = 0; i < count[1]; i++)
      //   nums[index++] = 1;
      // for(int i = 0; i < count[2]; i++)
      //   nums[index++] = 2;

      int zero = -1;         // nums[0...zero] == 0
      int two = nums.size(); // nums[two...n-1] == 2
      for(int i = 0; i < two; ) {
        if(nums[i] == 1)
          i++;
        else if(nums[i] == 2) {
          two--;
          swap(nums[i], nums[two]);
        }
        else{ // nums[i] == 0
          assert(nums[i] == 0);
          zero++;
          swap(nums[zero], nums[i]);
          i++;
        }
      }
    }
};
int main(){
  int arr[] = {0, 1, 0, 2, 1, 0};
  vector<int> vec(arr, arr + sizeof(arr)/sizeof(int));
  Solution().sortColors(vec);
  for(int i = 0; i < vec.size(); i++)
    cout << vec[i] << " ";
  cout << endl;
  return 0;
}
