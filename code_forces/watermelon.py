def func(w):
    if w==2:
        return 'NO'
    if not w&1:
        return 'YES'
    if w&1:
        return 'NO'
w=int(input())
print(func(w))