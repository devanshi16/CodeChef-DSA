t = int(input())
for _ in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    seq = [int(x) for x in list(input().split())]
    check = []
    output = [len(seq)]
    for i in range(k):
        check.append(i+1)
    for i in range(n):
        sub = seq[:i + 1]
        if ((set(check).issubset(set(sub)))) :
            output.append(i)
    print(min(output))