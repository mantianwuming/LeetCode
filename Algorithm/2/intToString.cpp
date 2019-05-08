#include <iostream>
using namespace std;
string intToString(int num){
  string s = '';
  if(num==0) return '0';
  if(num < 0){
    num = -1 * num;
    while(num){
      s += '0' + num%10;
      num /= 10;
    }
    s += '-'
    reverse(s);
    return s;
  }
  while(num){
    s += '0' + num%10;
    num /= 10;
  }
  reverse(s);
  return s;
}
