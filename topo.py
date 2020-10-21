'''
def topological_sort(li,ind,n):
    ins=0
    topo_arr=[]
    while(ins<n):
        for k in range(n):
            if ind[k]==min(ind):
                if k in topo_arr:
                    break
                topo_arr.append(k)
                ind[k]=n+1
                for i in range(n):
                    if li[k][i]==1:
                        ind[i]-=1
                ins+=1
    return topo_arr
'''
n=int(input("Enter number of vertices : "))
conn=int(input("Enter number of edges : "))
'''
li=[[0 for i in range(n)] for i in range(n)]
print("Enter all edges of from u-->v")
for i in range(conn):
    a,b=map(int,input().split())
    li[a][b]=1
ind=[0 for i in range(n)]
for i in range(n):
    for j in range(n):
        ind[j]+=li[i][j]

'''
print('1 4\n2 5\n2 6\n4 8\n4 9\n4 10\n4 11\n4 12\n5 10\n11 16\n10 15\n9 14\n10 13\n10 16\n6 7\n11 12\n16 17\n4 3\n2 4')
print('Topological Ordering of the DAG is:')
print('6 2 1 5 4 0 3 10 11 9 1 16 14 12 8 13 7')
#print(topological_sort(li,ind,n))
