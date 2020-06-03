t = int(input())
for _ in range(t):
    n = int(input())
    profit = []
    for i in range(n):
        s, p, v = input().split()
        s, p, v = int(s), int(p), int(v)
        profit.append((p//(s+1))*v)
    print(max(profit))