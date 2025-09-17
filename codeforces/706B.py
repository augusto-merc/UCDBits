def merge(arr, value, left, mid, right):
    if abs(left - right) <= 1:
        return mid
    if value < arr[mid]:
        return merge(arr, value, left, (left + mid) // 2, mid)
    elif value >= arr[mid]:
        return merge(arr, value, mid, (mid + right) // 2, right)
    
    ...
    

n = int(input())

x = list(map(int, input().split()))
x.sort()

q = int(input())
r = []

for i in range(q):
    m = int(input())
    
    ind = merge(x, m, 0, n // 2, n - 1)
    if ind == 0:
        if m < x[0]:
            r.append(0)
        else:
            r.append(1)
    else:
        r.append(ind+1)
    
    ...

    
print(*r, sep='\n')
