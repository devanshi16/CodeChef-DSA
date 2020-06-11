t = int(input())
for _ in range(t):
    n, z = input().split()
    n, z = int(n), int(z)
    a = [int(x) for x in input().split()]
    count = s = 0
    x=[]
    for i in a :
        while (i>0) :
            x.append(i)
            i = i//2
    x.sort(reverse = True)
    for i in x:
        z -= i
        count += 1
        if z <= 0:
            print(count)
            s = 1
            break
    if s == 0:
        print("Evacuate")