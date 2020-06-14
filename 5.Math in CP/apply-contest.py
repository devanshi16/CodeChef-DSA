import math
for _ in range(int(input())):
    n, a, b, k = list(map(int,input().split()))
    x = (a*b)//math.gcd(a, b)
    y = n//a + n//b - 2*(n//x)
    if(y>=k):
        print("Win")
    else:
        print("Lose")