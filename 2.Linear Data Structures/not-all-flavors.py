t = int(input())
for _ in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    seq = [int(x) for x in list(input().split())]
    check = []
    output = []
    for i in range(k):
        check.append(i+1)
    for i in range(n):
        sub = seq[:i + 1]
        if ((set(check).issubset(set(sub)))) :
            output.append(i)
    print(min(output))


t=int(input())
while t>0 :
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=[]
    for i in range(k+1) :
        s.append(0)
    an=0
    for i in range(n) :
        c=i-s[l[i]]
        if c>an :
            an=c
        s[l[i]]=i+1
    for i in range(1,k+1) :
        c=n-s[i]
        if c>an :
            an=c
    print(an)
    t-=1