t = int(input())
for _ in range(t):
    activity, origin = input().split()
    activity, origin = int(activity), str(origin)
    points = 0
    for i in range(activity):
        act = list(map(str,input().split(' ')))
        if (act[0] == 'CONTEST_WON'):
            if (int(act[1]) < 20):
                points = points + 300 + (20 - int(act[1]))
            else:
                points += 300        
        elif (act[0] == 'TOP_CONTRIBUTOR'):
            points += 300
        elif (act[0] == "BUG_FOUND"):
            points += int(act[1])
        elif (act[0] == 'CONTEST_HOSTED'):
            points += 50
    if (origin == 'INDIAN'):
        month = points//200
    else:
        month = points//400
    print(month)