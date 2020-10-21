#include<iostream>
#include<queue>
using namespace std;
#define N 4 
#define M 3
class node{
public:
	int r;
	int c;
	int val;
	node(int x,int y,int z)
	{
		r=x;
		c=y;
		val=z;
	}
};
int mind(char gr[M][N])
{
	node src(0,0,0);
	bool visited[M][N];
	for (int i = 0; i < N; i++) { 
        for (int j = 0; j < M; j++) 
        {
        	if(gr[i][j]=='0')
        	{
        		visited[i][j]=false;
			}
			else
        	{
        		visited[i][j]=false;
			}
			if(gr[i][j]=='s')
			{
				src.r=i;
				src.c=j;
			}
        }
    }
    queue<node> q;
    q.push(src);
    visited[src.r][src.c]=true;
    while(!q.empty())
    {
    	node p=q.front();
    	q.pop();
    	if(gr[p.r][p.c]=='d')
    	{
    		return p.val;
		}
		
		if(p.r-1>=0 && visited[p.r-1][p.c]==false){
			q.push(node(p.r-1,p.c,p.val+1));
			visited[p.r-1][p.c]=true;
		}
		if(p.c-1>=0 && visited[p.r][p.c-1]==false){
			q.push(node(p.r,p.c-1,p.val+1));
			visited[p.r][p.c-1]=true;
		}
		if(p.r+1<M && visited[p.r+1][p.c]==false){
			q.push(node(p.r+1,p.c,p.val+1));
			visited[p.r+1][p.c]=true;
		}
		if(p.c+1<N && visited[p.r][p.c+1]==false){
			q.push(node(p.r,p.c+1,p.val+1));
			visited[p.r][p.c+1]=true;
		}
		
	}
    return -1;
    
}
int main()
{
	char grid[M][N] = { { '0', '*', '0', 's' }, 
                        { '*', '0', '*', '*' }, 
                        { 'd', '*', '*', '*' } };
    cout<<mind(grid);
	return 0;
}
