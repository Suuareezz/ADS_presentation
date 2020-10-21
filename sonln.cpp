#include<iostream>
using namespace std;
int max(int a,int b){return a>b?a:b;}
int *root,*count;
int find(int i)
{
    while(i!=root[i])
    {
        i = root[i];
    }
    return i;
}
void onion(int x,int y)
{
    if(x!=y)
    {
        root[y] = x;
        count[x] += count[y];
        count[y] = 0;
    }
}
int main()
{
    int n;
    cin>>n;
    root = new int[2*n+1];
    count = new int[2*n+1];
    for(int i=0;i<2*n+1;i++)
    {
        root[i] = i;
        count[i] = 1;
    }
    for(int i=0;i<n;i++)
    {
        int a,b;
        cin>>a>>b;
        int x = find(a-1);
        int y = find(b-1);
        onion(x,y);
    }
    int mincount = 2*n+1;
    int maxcount = 0;
    for(int i=0;i<2*n+1;i++)
    {
        if(count[i]>1 && count[i]<mincount)
        {
            mincount = count[i];
        }
        if(count[i]>maxcount)
        {
            maxcount = count[i];
        }
    }
    cout<<mincount<<" "<<maxcount;
}