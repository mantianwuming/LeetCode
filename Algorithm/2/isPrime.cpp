#include <iostream>
using namespace std;
bool isPrime(int n){
  for(int x = 2; x*x <= n; x++)
    if(n%x == 0)
      return false;
  return true;
}

bool isPrime(int n){
  if(n == 0 || n == 1) return false;
  if(n == 2) return true;
  if(n < 0) return false;
  if(n%2 == 0) return false
  for(int x = 3; x*x <= n; x += 2)
    if(n%x == 0)
      return false;
  return true;
}
