t = int(input())
for test in range(t):
    n = int(input())

    speed = list(map(int,input().split()))
    for i in range(1,len(speed)):
        if speed[i]>speed[i-1]:
            speed[i] = speed[i-1]
            
    speed = set(speed)
    print(len(speed))
