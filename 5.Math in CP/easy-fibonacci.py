for _ in range(int(input())):
    n = int(input())
    fibo = [0,1]
    for i in range(2,n):
        fibo.append((fibo[i-2]+fibo[i-1])%10)
    print(fibo[len(fibo)//2])
    #or
    #temp = 1
    #while(temp*2 <= n):
    #    temp *= 2
    #temp -= 1
    #print(fibo[temp%60]) when sequence has size of 60 