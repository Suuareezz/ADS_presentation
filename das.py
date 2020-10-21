
def find(numb):
    
    


def uni(a,b):


global uval=[]
global uval_index=[]
n=int(input())
val=[]
for i in range(n):
    args=list(map(int,input().split()))
    val.append(args[0])
    val.append(args[1])
uval=[]
uval_index=[]
for i in val:
    if i not in uval:
        uval.append(i)
        uval_index.append(i)

for i in range(0,len(val),2):
    f1=find(val[i])
    f2=find(val[i+1])
    union(f1,f2)





