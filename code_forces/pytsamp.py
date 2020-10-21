from collections import Counter 
def substr(st):
    n=len(st)
    so=0
    for i in range(n):
        for j in range(n-i+1):
            if unq(st[i:i+j]):
                if so<len(st[i:i+j]):
                    so=len(st[i:i+j])
    return so
def unq(st):
    abc=Counter(st)
    if True if i==1 for all i in abc.values()) else False:
        return True
    return False

strr='geeksforgeeks'
print(substr(strr))