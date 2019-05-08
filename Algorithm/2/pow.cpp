#include <iostream>

using namespace std;

double pow(double x, int n){
  assert(n >= 0);
  if(n == 0)
    return 1.0;
  double t = pow(x, n/2);
  if(n % 2)
    return x*t*t;
  return t*t;
}
