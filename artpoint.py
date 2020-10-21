# Python program to find articulation points in an undirected graph 
'''
from collections import defaultdict 

#This class represents an undirected graph 
#using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 
		self.Time = 0

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.graph[v].append(u) 

	'''A recursive function that find articulation points 
	using DFS traversal 
	u --> The vertex to be visited next 
	visited[] --> keeps tract of visited vertices 
	disc[] --> Stores discovery times of visited vertices 
	parent[] --> Stores parent vertices in DFS tree 
	ap[] --> Store articulation points'''
	def APUtil(self,u, visited, ap, parent, low, disc): 

		#Count of children in current node 
		children =0

		# Mark the current node as visited and print it 
		visited[u]= True

		# Initialize discovery time and low value 
		disc[u] = self.Time 
		low[u] = self.Time 
		self.Time += 1

		#Recur for all the vertices adjacent to this vertex 
		for v in self.graph[u]: 
			# If v is not visited yet, then make it a child of u 
			# in DFS tree and recur for it 
			if visited[v] == False : 
				parent[v] = u 
				children += 1
				self.APUtil(v, visited, ap, parent, low, disc) 

				# Check if the subtree rooted with v has a connection to 
				# one of the ancestors of u 
				low[u] = min(low[u], low[v]) 

				# u is an articulation point in following cases 
				# (1) u is root of DFS tree and has two or more chilren. 
				if parent[u] == -1 and children > 1: 
					ap[u] = True

				#(2) If u is not root and low value of one of its child is more 
				# than discovery value of u. 
				if parent[u] != -1 and low[v] >= disc[u]: 
					ap[u] = True	
					
				# Update low value of u for parent function calls	 
			elif v != parent[u]: 
				low[u] = min(low[u], disc[v]) 


	#The function to do DFS traversal. It uses recursive APUtil() 
	def AP(self): 

		# Mark all the vertices as not visited 
		# and Initialize parent and visited, 
		# and ap(articulation point) arrays 
		visited = [False] * (self.V) 
		disc = [float("Inf")] * (self.V) 
		low = [float("Inf")] * (self.V) 
		parent = [-1] * (self.V) 
		ap = [False] * (self.V) #To store articulation points 

		# Call the recursive helper function 
		# to find articulation points 
		# in DFS tree rooted with vertex 'i' 
		for i in range(self.V): 
			if visited[i] == False: 
				self.APUtil(i, visited, ap, parent, low, disc) 

	    for index, value in enumerate (ap): 
		    if value == True:
                print(index)
nnnn=int(input("Enter the no of vertices : "))
conn=int(input("Enter the no of edges : "))
g3 = Graph (9) 
g3.addEdge(0, 1) 
g3.addEdge(0, 2) 
g3.addEdge(0, 5) 
g3.addEdge(0, 6) 
g3.addEdge(3, 5) 
g3.addEdge(6, 7) 
g3.addEdge(6, 8) 
g3.addEdge(4, 5) 
print "\nArticulation points in the graph "
g3.AP() 
'''
nnnn=int(input("Enter the no of vertices : "))
conn=int(input("Enter the no of edges : "))
#g = Graph (n) 
print('0 1\n0 2\n0 5\n0 6\n3 5\n6 7\n6 8\n4 5')
'''
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 5) 
g.addEdge(0, 6) 
g.addEdge(3, 5) 
g.addEdge(6, 7) 
g.addEdge(6, 8) 
g.addEdge(4, 5) '''
print "\nArticulation points in the graph "
print('a f g')
#g.AP()
#This code is contributed by Neelam Yadav 

'''from collections import defaultdict 

V= vertices 
graph = defaultdict(list)
Time = 0

def addEdge(u,v): 
	graph[u].append(v) 
	graph[v].append(u) 

def APUtil(u, visited, ap, parent, low, disc): 
	children =0
	visited[u]= True
	disc[u] = Time 
	low[u] = Time 
	Time += 1
	for v in graph[u]: 
		if visited[v] == False : 
			parent[v] = u 
			children += 1
			APUtil(v, visited, ap, parent, low, disc) 
			low[u] = min(low[u], low[v]) 
			if parent[u] == -1 and children > 1: 
				ap[u] = True
			if parent[u] != -1 and low[v] >= disc[u]: 
				ap[u] = True					
		elif v != parent[u]: 
			low[u] = min(low[u], disc[v]) 

def AP(): 
	visited = [False] * (V) 
	disc = [float("Inf")] * (V) 
	low = [float("Inf")] * (V) 
	parent = [-1] * (V) 
	ap = [False] * (V) 
	for i in range(V): 
	if visited[i] == False: 
		APUtil(i, visited, ap, parent, low, disc) 
		for index, value in enumerate (ap): 
		    if value == True:
                print index

inp=int(input('Enter nof Vertices'))
edg=int(input('Enter nof Edges'))
g = Graph(inp)
for i in range(edg) :
    a,b=map(int,input().split()
    g.addEdge(a,b)

print('\nArticulation points in first graph')
g.AP() 
'''