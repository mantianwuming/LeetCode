#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void moveZeroes(vector<int>& nums) {
    // vector<int> nonZeroElements;
    //
    // for(int i = 0; i < nums.size(); i++)
    //   if(nums[i])
    //     nonZeroElements.push_back(nums[i]);
    //   for(int i = 0; i < nonZeroElements.size(); i++)
    //     nums[i] = nonZeroElements[i];
    //   for(int i = nonZeroElements.size(); i < nums.size(); i++)
    //     nums[i] = 0;

    // int k = 0; // nums�У�[0...k)��Ԫ�ؾ�Ϊ��0Ԫ��
    // // ��������i��Ԫ�غ󣬱�֤[0...i]�����з�0Ԫ�أ� ������˳��������[0...k)��
    // for(int i = 0; i < nums.size(); i++)
    //   if(nums[i])
    //     nums[k++] = nums[i];
    //
    // // ��numsʣ���λ�÷���Ϊ0
    // for(int i = k; i < nums.size(); i++)
    //   nums[i] = 0;

    int k = 0; // nums�У�[0...k)��Ԫ�ؾ�Ϊ��0Ԫ��
    // ��������i��Ԫ�غ󣬱�֤[0...i]�����з�0Ԫ�أ� ������˳��������[0...k)��
    // ͬʱ��[k...i]Ϊ0
    for(int i = 0; i < nums.size(); i++)
      if(nums[i])
        if(i != k)
          swap(nums[k++], nums[i]);
        else
          k++;
  }
};

int main() {
  int arr[] = {0, 1, 0, 3, 12};
  vector<int> vec(arr, arr + sizeof(arr)/sizeof(int));
  Solution().moveZeroes(vec);
  for(int i = 0; i < vec.size(); i++)
    cout << vec[i] << " ";
  cout << endl;
  return 0;
}
