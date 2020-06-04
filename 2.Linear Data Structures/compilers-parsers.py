t = int(input())
for _ in range(t):
    tags = str(input())
    test = []
    count = 0
    for i in tags:
        if(i == '<'):
            test.append(i)
            count += 1
        elif(i == '>'):
            if (len(test) == 0):
                break
            else:
                count += 1
                test.pop()
    print(count)