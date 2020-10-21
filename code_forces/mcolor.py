from collections import defaultdict

def get_ans(v, colors, e, e_arr):
    
    # dict to store neighbours of each vertex in a set
    neighbours_set_dict = defaultdict(lambda: set())
    for i in range(0,2*e,2):
        neighbours_set_dict[e_arr[i]].add(e_arr[i+1])
        neighbours_set_dict[e_arr[i+1]].add(e_arr[i])
        
    
    def recurse(colored, vertex, remaining_vertex):
        # remaining_vertex stores number of un-painted vertices
        if remaining_vertex == 0 or vertex > v:
            return True
        
        # If vertex not already colored
        if colored[vertex] == -1:
            
            # Try every color
            for c in list(range(colors)):
                
                # to store if neighbour has same color
                same_color = False
                
                for neighbour in neighbours_set_dict[vertex]:
                    if colored[neighbour] == c:
                        same_color = True
                        
                if not same_color:
                    
                    # Color the vertex and decrease remaining_vertex by 1
                    colored[vertex] = c
                    remaining_vertex -= 1
                    
                    # With the color 'c' for current vertex try coloring
                    # next vertex, i.e., vertex+1
                    if recurse(colored, vertex+1, remaining_vertex):
                        return True
        
        return False
    
    # Stores color assigned to each vertex
    colored = defaultdict(lambda: -1)
    
    return 1 if recurse(colored, 1, v) else 0

v = int(input())
colors = int(input())
e = int(input())
e_arr = list(map(int, input().split()))
print(get_ans(v, colors, e, e_arr))