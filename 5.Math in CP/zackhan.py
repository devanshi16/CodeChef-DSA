import math
for _ in range(int(input())):
    l, b = list(map(int,input().split()))
    print(math.gcd(l,b))