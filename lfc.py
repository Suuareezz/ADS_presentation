n=int(input("Enter the no of vertices : "))
conn=int(input("Enter the no of edges : "))
listy=[[0]*n for i in range(n)]
print("Enter the connections one by one in the format source to destination")
for i in range(conn):
    a,b=map(int,input().split())
    listy[a][b]=1
indeg=[0]*n
for i in range(n):
    for j in range(n):
        indeg[j]+=listy[i][j]
count=0
final=[]
while(count<n):
    for k in range(n):
        if indeg[k]==min(indeg):
            if k in final:
                break
            final.append(k)
            indeg[k]=n+1
            for i in range(n):
                if listy[k][i]==1:
                    indeg[i]-=1
            count+=1
print(final)