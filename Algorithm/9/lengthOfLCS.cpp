#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLCS(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();

        if(m == 0 || n == 0)
            return 0;

        vector<vector<int>> memo(m, vector<int>(n, 0));

        for(int i = 0; i < n; i ++)
            if(s1[0] == s2[i]){
                memo[0][i] = 1;
                for(int x = i; x < n; x++)
                    memo[0][x] = 1;
                }
        for(int j = 0; j < m; j++)
            if(s1[j] == s2[0]){
                memo[j][0] = 1;
                for(int x = j; x < m; x++)
                    memo[x][0] = 1;
            }

        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++){
                if(s1[i] == s2[j])
                    memo[i][j] = memo[i-1][j-1] + 1;
                else
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1]);
            }
        return memo[m-1][n-1];
    }
};

int main(){

    return 0;
}
