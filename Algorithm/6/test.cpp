#include<iostream>
using namespace std;

int Add(int a,int b)//1
{
    return a+b;
}

char Add(char a,char b)//2
{
    return a+b;
}

int main()
{
    cout<<Add(666,888)<<endl;//1
    cout<<Add('1','2');//2
    return 0;
}
