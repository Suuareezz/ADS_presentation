def heapify(i):
    left = 2*i+1
    right = 2*i+2
    if left<len(arr) and right<len(arr):
        x = min(arr[i],min(arr[left],arr[right]))
        if x==arr[i]:
            return arr
        elif x==arr[left]:
            arr[i],arr[left] = arr[left],arr[i]
            heapify(left)
        elif x==arr[right]:
            arr[i],arr[right] = arr[right],arr[i]
            heapify(right)
def build():
    for i in range(len(arr)//2,-1,-1):
        heapify(i)

def check():
    for i in range(len(arr)):
        if 2*i+1<len(arr) and 2*i+2<len(arr):
            if arr[2*i+1]<arr[i] or arr[2*i+2]<arr[i]:
                print('Not a binary min heap')
                return False
    return True

arr = list(map(int,input().split()))
if True:
    build()
    print(arr)
