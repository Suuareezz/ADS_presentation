from collections import defaultdict 
V= vertices
graph = defaultdict(list) 


def addEdge(u,v): 
    graph[u].append(v) 

def DFSUtil(v,visited): 	 
	visited[v]= True
	print v, 		
	for i in graph[v]: 
		if visited[i]==False:
            DFSUtil(i,visited) 

def fillOrder(v,visited, stack):		
	visited[v]= True
	for i in self.graph[v]: 
		if visited[i]==False: 
            self.fillOrder(i, visited, stack) 
	stack = stack.append(v) 

def getTranspose(): 
	g = Graph(.V) 
	for i in graph: 
		for j in graph[i]: 
			g.addEdge(j,i) 
	return g 

def printSCCs(): 
	
	stack = [] 
	visited =[False]*(V) 
	for i in range(V): 
		if visited[i]==False: 
			fillOrder(i, visited, stack) 
	gr = getTranspose() 
	visited =[False]*(V) 
	while stack: 
		i = stack.pop() 
		if visited[i]==False: 
			gr.DFSUtil(i, visited) 
			print"" 
inp=int(input('Enter nof Vertices'))
edg=int(input('Enter nof Edges'))
g = Graph(inp)
for i in range(edg) :
    a,b=map(int,input().split()
    g.addEdge(a,b)

print ("The strongly connected components in the given graph") 
g.printSCCs() 

