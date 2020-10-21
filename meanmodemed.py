n=int(input())
li=list(map(int,input().split()))

mean=sum(i for i in li)
mean=mean/n
print(mean)
sli=sorted(li)
lenn=len(sli)//2
median=sli[lenn]+sli[lenn-1]
median=median/2
print(median)

newli=[]
for i in li:
    print(li.count(i))
for i in li:
    if len(newli)>0:
        if(newli.count(i)<1):
            newli.append(i)
    else:
        newli.append(i)

snt=[0 for i in range(len(newli))]
newli=sorted(newli)
for i in range(len(newli)):
    snt[i]=li.count(newli[i])
note=0
noti=0
maxi=1
for i in range(len(snt)):
    if snt[i]>maxi:
        maxi=snt[i]
        noti=i

if(maxi==1):
    print(newli[0])
else:
    print(newli[noti])




