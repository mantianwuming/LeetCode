
#include<queue>
#include<vector>
#include<iostream>
using namespace std;

struct node
{
    int x, y;
    node(int x,int y):x(x),y(y){}
};

struct cmp
{
    bool operator()(node a,node b)
    {
        if(a.x == b.x)  return a.y >= b.y;
        else return a.x > b.x;
    }
};

int main()
{
    priority_queue<node,vector<node>,cmp> pq;    //带有三个参数的优先队列;
    for(int i = 1; i <= 5; i++)
        for(int j = 1; j <= 5; j++)
            pq.push(node(i,j));
    while(!pq.empty())
    {
        cout<<pq.top().x<<" "<<pq.top().y<<endl;
        pq.pop();
    }
    return 0;
}
