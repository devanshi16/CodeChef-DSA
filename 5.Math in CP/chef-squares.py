import math
for _ in range(int(input())):
    n = int(input())
    x = 100000000
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:  #if i is a factor
            if (n // i) - i != 0 and ((n // i) - i) % 2 == 0:
                x = min(x, ((n // i) - i) // 2)
    print(x * x if x != 100000000 else -1)