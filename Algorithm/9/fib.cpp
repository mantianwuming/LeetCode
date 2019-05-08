#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

vector<int> memo;
int num = 0;

// 记忆化搜索
int fib(int n){
    num++;
    if(n == 0)
        return 0;
    if(n == 1)
        return 1;
    if(memo[n] == -1)
        memo[n] = fib(n-1) + fib(n-2);

    return memo[n];
}

// 动态规划
int fib1(int n){
    vector<int> memo(n+1, -1);
    memo[0] = 0;
    memo[1] = 1;
    for(int i = 2; i <= n; i++)
        memo[i] = memo[i=1] + memo[i-2];
    return memo[n];
}

int fib2(int n){
    if(n == 0)
        return 0;
    if(n == 1)
        return 1;
    int a = 0;
    int b = 1;
    int res = 0;
    for(int i = 2; i <= n; i++){
        res = a + b;
        a = b;
        b = res;
    }
    return res;
}

int main(){
    num = 0;
    int n = 20;
    memo = vector<int>(n+1, -1);
    time_t startTime = clock();
    int res = fib2(n);
    time_t endTime = clock();

    cout << "fib(" << n << ") = " << res << endl;
    cout << "time : " << double(endTime - startTime)/CLOCKS_PER_SEC << " s" << endl;
    cout << "run function fib() " << num << "times" << endl;

    return 0;
}
