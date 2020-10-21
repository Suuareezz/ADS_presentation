tc=int(input())
for t in range(tc):
    m,tc,th=map(int,input().split(' '))
    for i in range(m):
        if tc==th:
            print('No')
        elif(tc<th):
            th-=1
            tc+=2
        else:
            th+=2
            tc-=1
    if tc!=th:
        print('Yes')