#include <iostream>

using namespace std;

int binarySearch(int arr[], int n, int target){
  int l = 0, r = n-1;
  while(l<=r){
    int mid = l + (r-l)/2;
    if(arr[mid] == target) return mid;
    if(arr[mid] > target) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
}

int binarySearch_recursion(int arr[], int l, int r, int target){
  if(l > r)
    return -1;
  int mid = l + (r - l) / 2;
  if(arr[mid] == target)
    return mid;
  else if(arr[mid] > target)
    return binarySearch_recursion(arr, l, mid-1, target);
  else
    return binarySearch_recursion(arr, mid+1, r, target);
}

int main() {
  int arrry[] = {1, 3, 5, 7, 9}, l = 0, r = 4, target = 5;
  cout << binarySearch_recursion(arrry, l, r, target) << endl;
}
