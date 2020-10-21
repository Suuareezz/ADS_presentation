n=int(input())
st=input()
i=0
c=0
if len(st)==1:
    print('0')
else:        
    while(True):
        if st[i]==st[i+1]:
            c+=1
        
        if i==n-2:
            break
        i+=1
    print(c)