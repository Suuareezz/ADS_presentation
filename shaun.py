# cook your dish here
from collections import defaultdict
tc=int(input())
for t in range(tc):
    Sum=int(input())
    arr=list(map(int,input().split()))
    res=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i<j:
                print(i,j+! )
                if sum(arr[i:j+1])==Sum:
                    res+=1
    print(res)