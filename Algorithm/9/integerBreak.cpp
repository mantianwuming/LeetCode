#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

// class Solution {
// private:
//     vector<int> memo;
//
//     int calc(int n){
//         memo[2] = 2;
//         memo[3] = 3;
//         int res = 0;
//         for(int i = 1; i < n; i++){
//             if(memo[i] == 0)
//                 res = (n-i) * calc(i);
//             else
//                 res = (n-i) * memo[i];
//             if(res > memo[n])
//                 memo[n] = res;
//         }
//         return memo[n];
//     }
// public:
//     int integerBreak(int n) {
//         if(n == 2)
//             return 1;
//         if(n == 3)
//             return 2;
//         memo = vector<int>(n+1, 0);
//         return calc(n);
//     }
// };

// class Solution {
// private:
//     vector<int> memo;
//
//     int max3(int a, int b, int c){
//         return max(a, max(b,c));
//     }
//
//     // ��n���зָ���ٷָ������֣������Ի�õ����˻�
//     int breakInteger(int n){
//         if(n == 1)
//             return 1;
//         if(memo[n] != -1)
//             return memo[n];
//         int res = -1;
//         for(int i = 1; i <= n-1; i++)
//             // i + (n-i)
//             res = max3(res, i*(n-i), i * breakInteger(n-i));
//         memo[n] = res;
//         return res;
//     }
// public:
//     int integerBreak(int n) {
//         assert(n >= 2);
//         memo = vector<int>(n+1, -1);
//         return breakInteger(n);
//     }
// };

class Solution {
private:
    int max3(int a, int b, int c){
        return max(a, max(b,c));
    }

public:
    int integerBreak(int n) {
        assert(n >= 2);

        // memo[i]��ʾ������i�ָ���ٷָ�������֣���õ������˻�
        vector<int> memo(n+1, -1);
        memo[1] = 1;
        for(int i = 2; i <= n; i++)
            // ���memo[i]
            for(int j = 1; j <= i-1; j++)
                // j + (i-j)
                memo[i] = max3(memo[i], j * (i-j), j*memo[i-j]);
        return memo[n];
    }
};

int main(){

}
