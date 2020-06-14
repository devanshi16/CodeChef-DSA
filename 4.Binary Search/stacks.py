def binary_search(ARR,X):
    first = 0
    last = len(ARR)-1
    k = -1
    while(first<=last):
        mid = (first+last)//2
        if(X<ARR[mid]):
            k = mid
            last = mid-1
        else:
            first = mid+1
            
    return k
for _ in range(int(input())):
        l = int(input())
        n = list(map(int,input().split()))
        stack = []
        for i in n:
            min_val = binary_search(stack,i)
            if min_val == -1:
                stack.append(i)
            else:
                stack[min_val] = i
            print(stack)