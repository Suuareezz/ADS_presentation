'''
def fair(listt,lis,indes):
    fifa=1
    for i in range(len(lis)):
        if not i==indes:
            if( set(listt) & set(lis[i])):
                lis[i]=listt + list(set(lis[i]) - set(listt))
                lis.pop(indes)
                fifa=2
                break
    if fifa==2:
        for i in lis:
            if listt==i:
                i=[]
                break
                
    return lis


n=int(input())
lis=[[] for i in range(2*n)]

for i in range(n):
    args=list(map(int,input().split()))
    flag=0
    for i in lis:
        if(args[0] in i):
            i.append(args[1])
            flag=1
            break
        elif(args[1] in i):
            i.append(args[0])
            flag=1
            break
    if flag==0:
        for i in lis:
            if len(i)==0:
                i.append(args[0])
                i.append(args[1])
                break

u=0
while(True):
    if not len(lis[u])==0:
        lis=fair(lis[u],lis,u)
        u=u+1
    if(len(lis[u])==0):
        break
cis=[]
mx=0
mn=2*n
for i in lis:
    if not len(i)==0:
        if(len(i)>mx):
            mx=len(i)
        if(len(i)<mn):
            mn=len(i)
print(mx,mn)


'''
inp=input().split(maxsplit=1)

print(type(inp[0]))
