n, m = input().split()
seq1 = [int(x) for x in input().split()]
seq2 = [int(x) for x in input().split()]
min1 = seq1.index(min(seq1))
max2 = seq2.index(max(seq2))
for i in range(int(n)) :
    print(i,max2)
for j in range(int(m)) :
    if j!=max2 :
        print(min1,j)