# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
li=list(map(int,input().split()))
li=sorted(li)
if not len(li)%2==0:
    q1=li[len(li)//2]
    l1=li[:len(li)//2]
    l2=li[len(li)//2:]
    q2=l1[len(l1)//2-1]+l1[len(l1)//2-1]/2
    q3=l2[len(l2)//2-1]+l2[len(l2)//2-1]/2
    print(q2)
    print(int(q1))
    print(q3)
else:
    q1=li[len(li)//2-1]+li[len(li)//2-1]/2
    l1=li[:len(li)//2]
    l2=li[len(li)//2+1:]
    q2=l1[len(l1)//2]
    q3=l2[len(l2)//2]
    print(q2)
    print(int(q1))
    print(q3)


