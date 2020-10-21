#include<iostream>
#include<list>
using namespace std;
class grapd{
public:
	int v;
	list<int> *adj;
	grapd(int vt){
		v=vt;
		adj=new list<int>[v];
		cout<<"contsr\n";
	}
	void addEdge(int a,int b){
		adj[a].push_back(b);
		cout<<"insert\n";
	}
	void dfsutil(int x,bool visited[])
	{
		
		visited[x]=true;
		
		cout<<x<<" ";
		list<int>::iterator i;
		for(i= adj[x].begin();i!=adj[x].end();i++){
			
			if(!visited[*i]){
				dfsutil(*i,visited);
			}
		}
	}
	void dfs(int s){
		bool visited[v];
		for(int op=0;op<v;op++){
			visited[op]=false;
		}
		dfsutil(s,visited);
	
		
	}    //O(V+E) space O(V)
	
};
int main(){
	grapd g(7);
	g.addEdge(1, 2); 
    g.addEdge(1, 3); 
    g.addEdge(1, 4); 
    g.addEdge(2, 5); 
    g.addEdge(3, 6); 
    g.addEdge(4, 7);
    g.dfs(1);
	return 0;
}
