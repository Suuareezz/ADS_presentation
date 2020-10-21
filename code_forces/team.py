n=int(input())
li=[]
for i in range(n):
    op=list(map(int,input().split()))
    li.append(op)
no=0
for i in li:
    a=sum(j for ij in i)
    if a > 2:
        no+=1
print(no)



