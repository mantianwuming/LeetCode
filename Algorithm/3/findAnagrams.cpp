#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int freq1[256] = {0};
        int freq2[256] = {0};
        int l = p.size();
        vector<int> res;
        for(int i = 0; i < s.size() - l + 1; i++){
            int j = i + l;
            for(int m = 0; m < l; m++){
                freq1[s[m+i]]++;
                freq2[p[m]]++;
            if(freq1 == freq2)
                res.push_back(i);
            }
        }
        return res;
    }
};

int main() {
    string s = "abceabc";
    string p = "abc";
    vector<int> res = Solution().findAnagrams(s, p);
    cout << res << endl;
    return 0;
}
