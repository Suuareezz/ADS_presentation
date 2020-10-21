def gg():
    nari=input()
    if len(nari)<=10:
        print(nari)
    else:
        strr=nari[0]
        strr+=str(len(nari)-2)
        strr+=nari[len(nari)-1]
        print(strr)
n=int(input())
for i in range(n):
    gg()