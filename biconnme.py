'''def dfs(visited,v,listy):
    visited[v]=True
    dfsa.append(v)
    for i in range(1,len(listy[v])):
        if listy[v][i]==1 and visited[i]==False:
            dfs(visited,i,listy)
'''
from collections import defaultdict 
Time=0
def isBCUtil(u, visited, parent, low, disc): 
    global Time
    children =0
    visited[u]= True
    disc[u] = Time 
    low[u] = Time 
    Time += 1
    
    for v in graph[u]: 
        if visited[v] == False : 
            parent[v] = u 
            children += 1
            if isBCUtil(v, visited, parent, low, disc): 
                return True
            low[u] = min(low[u], low[v]) 
            if parent[u] == -1 and children > 1: 
                return True
            if parent[u] != -1 and low[v] >= disc[u]: 
                return True    
        elif v != parent[u]: 
                low[u] = min(low[u], disc[v]) 
  
    return False

def isBC():
    visited = [False] * (n) 
    disc = [float("Inf")] * (n) 
    low = [float("Inf")] * (n) 
    parent = [-1] * (n) 
    if isBCUtil(0, visited, parent, low, disc): 
        return False
    if any(i == False for i in visited): 
        return False
       
    return True
    

n=int(input("Enter the no of vertices : "))
conn=int(input("Enter the no of edges : "))
graph=defaultdict(list)
#[[0 for i in range(n+1)] for i in range(n+1)]
print("Enter the connections one by one in the format source to destination")
nodes=[]
for i in range(conn):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    if a not in nodes:
        nodes.append(a)
    if b not in nodes:
        nodes.append(b)
print(isBC())
'''
for i in listy:
    print(i)
print(nodes)
visited=[False for i in range(n+1)]
dfsa=[]
dfs(visited,nodes[0],listy)
disc=[0 for i in range(n)]
for i in range(len(dfsa)):
    disc[dfsa[i]-1]=i+1
print(dfsa,disc)

'''