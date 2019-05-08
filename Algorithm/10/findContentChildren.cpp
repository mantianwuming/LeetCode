#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end(), greater<int>());
        sort(s.begin(), s.end(), greater<int>());

        int si = 0, gi = 0;
        int res = 0;
        while(gi < g.size() && si < s.size()){
            if(s[si] >= g[gi]){
                res++;
                si++;
                gi++;
            }
            else
                gi++;
        }
        return res;
    }
};

class Solution1 {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int si = s.size()-1, gi = g.size()-1;
        int res = 0;
        while(gi >= 0 && si >= 0){
            if(s[si] >= g[gi]){
                res++;
                si--;
                gi--;
            }
            else
                gi--;
        }
        return res;
    }
};

int main(){
    int g1[] = {1, 2, 3};
    vector<int> g(g1, g1 + sizeof(g1)/sizeof(int));
    int s1[] = {1, 1};
    vector<int> s(s1, s1 + sizeof(s1)/sizeof(int));
    int res = Solution1().findContentChildren(g,s);
    cout << res << endl;
    return 0;
}
