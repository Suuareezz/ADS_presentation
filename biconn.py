from collections import defaultdict 
Time=0
def findconn(u, visited, parent, low, disc): 
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
            if findconn(v, visited, parent, low, disc): 
                return True
            low[u] = min(low[u], low[v]) 
            if parent[u] == -1 and children > 1: 
                return True
            if parent[u] != -1 and low[v] >= disc[u]: 
                return True    
        elif v != parent[u]: 
                low[u] = min(low[u], disc[v]) 
    return False
def biconn():
    visited = [False] * (n) 
    disc = [float("Inf")] * (n) 
    low = [float("Inf")] * (n) 
    parent = [-1]*(n) 
    if findconn(0, visited, parent, low, disc): 
        return False
    if any(i == False for i in visited): 
        return False
    return True
    
n=int(input("Enter the no of vertices : "))
conn=int(input("Enter the no of edges : "))
graph=defaultdict(list)
print("Enter the connections one by one in the format source to destination")
for i in range(conn):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(biconn())
