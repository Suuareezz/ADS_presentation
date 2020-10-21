#include<iostream>
#include<list>
using namespace std;
class graph{
public:
	int v;
	list<int> *adj;
	graph(int vt){
		v=vt;
		adj=new list<int>[v];
		cout<<"contsr\n";
	}
	void addEdge(int a,int b){
		adj[a].push_back(b);
		cout<<"insert\n";
	}
	void bfs(int s){
		bool visited[v];
		for(int op=0;op<v;op++){
			visited[op]=false;
		}
		cout<<"bfs out\n";
		list<int> q;
		visited[s]=true;
		q.push_back((s));
		list<int>::iterator it;
		while(!q.empty()){
			cout<<"bfs in\n";
			s=q.front();
			cout<<s<<" ";
			q.pop_front();
			for(it=adj[s].begin();it!=adj[s].end();it++){
				if(!visited[*it]){
					visited[*it]=true;
					q.push_back(*it);
				}
			}
		}
		
	}
	//O(V+E)
};
int main(){
	graph g(4);
	g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    g.addEdge(2, 0); 
    g.addEdge(2, 3); 
    g.addEdge(3, 3);
    g.bfs(2);
	return 0;
}
