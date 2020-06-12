def subarray(arr):
    S, a = [], 1
    S.append(a)
    for i in range(2,n+1):
        if arr[i]%arr[i-1]!=0:
            a += 1
        S.append(a)
    return S

n,q = map(int,input().split())
arr = list(map(int,input().split()))
arr.insert(0,0)
S = []
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        arr[query[1]] = query[2]
        S = subarray(arr)
    elif query[0] == 2:
        a = S[query[1]-1]
        print(S.index(a)+1)
    