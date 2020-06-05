n = int(input())
seq = list(input().split())
a = []
max_length = depth = max_pos = start = 0
for pos,i in enumerate(seq):
    if (i == '1'):
        a.append(i)
    else:
        a.pop()
    length = len(a)
    if (length > depth):
        depth = length
        index = pos + 1
    if len(a)==0:
        if pos - start + 1 > max_length:
            max_length = pos - start + 1
            max_pos = start + 1
            print(start, pos, max_length, max_pos)

        start= pos + 1
print(depth, index, max_length, max_pos)