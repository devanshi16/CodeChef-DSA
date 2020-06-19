for _ in range(int(input())):
    n, m, x, y = list(map(int,input().split()))
    if ((n-1)==1 and (m-1)==1):
        print("Chefirnemo")
    elif(((n-1)%x == 0) and ((m-1)%y == 0)):
        print("Chefirnemo")
    elif(((n-2)%x == 0) and ((m-2)%y == 0) and (n>=2 and m>=2)):
        print("Chefirnemo")
    else:
        print("Pofik")