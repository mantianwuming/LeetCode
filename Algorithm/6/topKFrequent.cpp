 #include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <cassert>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        assert( k > 0);

        // ͳ��ÿ��Ԫ�س��ֵ�Ƶ��
        unordered_map<int, int> freq;
        for(int i = 0; i < nums.size(); i++)
            freq[nums[i]]++;
        assert(k <= freq.size());

        // ɨ��freq��ά����ǰ����Ƶ����ߵ�k��Ԫ��
        // �����ȶ����У�����Ƶ�������������ݶ���(Ƶ�ʣ�Ԫ��)����ʽ
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for(unordered_map<int, int>::iterator iter = freq.begin(); iter != freq.end(); iter++){
            if(pq.size() == k){
                if(iter->second > pq.top().first){
                    pq.pop();
                    pq.push(make_pair(iter->second, iter->first));
                }
            }
            else
                pq.push(make_pair(iter->second, iter->first));
        }

        vector<int> res;
        while(!pq.empty()){
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        assert( k > 0);

        // ͳ��ÿ��Ԫ�س��ֵ�Ƶ��
        unordered_map<int, int> freq;
        for(int i = 0; i < nums.size(); i++)
            freq[nums[i]]++;
        assert(k <= freq.size());

        // ɨ��freq��ά����ǰ����Ƶ����ߵ�k��Ԫ��
        // �����ȶ����У�����Ƶ�������������ݶ���(Ƶ�ʣ�Ԫ��)����ʽ
        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq;
        vector<int> res;
        int n=0;
        for(unordered_map<int, int>::iterator iter = freq.begin(); iter != freq.end(); iter++)
            n++;
        for(unordered_map<int, int>::iterator iter = freq.begin(); iter != freq.end(); iter++){
            if(pq.size() == n - k){
                if(iter->second < pq.top().first){
                    res.push_back(pq.top().second);
                    pq.pop();
                    pq.push(make_pair(iter->second, iter->first));
                }
                else
                    res.push_back(iter->first);
            }
            else
                pq.push(make_pair(iter->second, iter->first));
        }
        return res;
    }
};
