n=6
li=['#' for i in range(n)]
ji=[' ' for i in range(n)]



for i in range(n):
    s="".join(ji[i:n-1])
    s=s+"".join(li[n-i-1:n])
    print(s)