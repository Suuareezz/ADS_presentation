import collections 
class Graph: 
    def __init__(self,v): 
        self.nv=v 
        self.graph=collections.defaultdict(list) 
        self.count=0 
    def checkbc(self):
        ss=self.nv
        visited=[False]*ss 
        d=[float('inf')]*ss 
        low=[float('inf')]*ss 
        parent=[-1]*ss 
        if self.biconfunc(0,visited,parent,low,d): 
            return False
        for i in visited:
            if not(i):
                return False
        return True
    def biconfunc(self,u,visited,parent,low,d): 
        children=0
        visited[u]=True
        d[u]=self.count 
        low[u]=self.count 
        self.count+=1
        for v in self.graph[u]: 
            if not(visited[v]): 
                parent[v]=u 
                children+=1
                if self.biconfunc(v,visited,parent,low,d): 
                    return True
                low[u]=min(low[u],low[v]) 
                if parent[u]==-1 and children>1: 
                    return True
                if parent[u]!=-1 and low[v]>=d[u]: 
                    return True	
            elif v!=parent[u]: 
                low[u]=min(low[u],d[v]) 
        return False
n=int(input("Enter the no of vertices"))
g=Graph(n)
e=int(input("Enter the no of edges"))
print("Enter the vertex pairs to which edges must be constructed")
for i in range(e):
    a,b=map(int,input().split())
    g.graph[a-1].append(b-1) 
    g.graph[b-1].append(a-1) 
dic={True:"It is biconnected",False:"Not biconnected"}
print(dic[g.checkbc()])
