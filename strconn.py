from collections import defaultdict
def dfsStack(v,visited,Gt): 
	visited[v]= True
	abb='abcdefghijklmnopqrstuvwxyz'
	print(abb[v],end='')
	for i in Gt[v]: 
		if visited[i]==False: 
			dfsStack(i,visited,Gt) 

def buildStack(v,visited,stack): 
    visited[v]= True
    for i in graph[v]: 
    	if visited[i]==False: 
    	    buildStack(i,visited,stack)
    stack = stack.append(v) 
	
def Transpose(): 
	g = defaultdict(list) 
	for i in graph: 
		for j in graph[i]: 
			g[j].append(i) 
	return g 
 
def SCC(): 		
    stack = [] 
    visited =[False]*(n)  
    for i in range(n): 
    	if visited[i]==False: 
    		buildStack(i,visited,stack) 
    Gt = Transpose() 
    visited =[False]*(n) 
    print('The Strongly Connected Components are:')
    while stack: 
    	i = stack.pop() 
    	if visited[i]==False: 
    		dfsStack(i,visited,Gt) 
    		print("")

n=int(input("Enter the no of vertices : "))
conn=int(input("Enter the no of edges : "))
graph=defaultdict(list)
print("Enter the connections one by one in the format source to destination")
for i in range(conn):
    a,b=map(int,input().split())
    graph[a].append(b)
print(SCC())
