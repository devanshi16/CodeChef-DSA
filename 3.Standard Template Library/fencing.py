for _ in range(int(input())):
    n, m, k = map(int,input().split())
    plants = []
    for i in range(k):
        a, b = map(int,input().split())
        plants.append([a,b])
    fence = x = y = 0
    for i in plants:
        x, y = i[0], i[1]
        fence += 4
        if [x+1,y] in plants:
            fence -= 1
        if [x-1,y] in plants:
            fence -= 1
        if [x,y+1] in plants:
            fence -= 1
        if [x,y-1] in plants:
            fence -= 1
    print(fence)

#Using Dictionaries:
#for _ in range(int(input())):
#    n, m, k = map(int,input().split())
#    plants = {}
#    for i in range(k):
#        a, b = map(int,input().split())
#        plants[(a,b)] ="*"
#    fence = x = y = 0
#    for i in plants:
#        x, y = i[0], i[1]
#        fence += 4
#        if (x+1,y) in plants:
#            fence -= 1
#        if (x-1,y) in plants:
#            fence -= 1
#        if (x,y+1) in plants:
#            fence -= 1
#        if (x,y-1) in plants:
#            fence -= 1
#    print(fence)