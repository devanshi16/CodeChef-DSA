#The two teams take shots alternately — team A shoots first, then team B shoots, then team A
#and so on until team B takes its N-th shot (at which point each team has taken exactly N
#shots). Even though all 2N shots are taken, the result of the shoot-out is often known earlier — e.g. if team A
#has already scored N−1 goals and team B has missed at least two shots, team A is definitely the winner.

#For each shot, you know whether it was a goal or a miss. You need to find the earliest moment when the winner is known — the smallest s
#(0≤s≤2N) such that after s shots, the result of the shoot-out (whether team A won, team B
#won or the match is drawn) would be known even if we did not know the results of the remaining 2N−s shots.

t = int(input())
for _ in range(t):
    s = int(input())
    n = str(input())
    ca = cb = 0
    pos = 0
    for i in range(len(n)):
        ra = (2*s-i-1)//2
        rb = 2*s-i-1-ra
        if (i%2==0):
            ca += int(n[i])
        else:
            cb += int(n[i])
        if (ca > (rb+cb)):
            print(i+1)
            pos = 1
            break
        elif (cb > (ra+ca)):
            print(i+1)
            pos = 1
            break
    if (pos == 0):
        print(len(n))
