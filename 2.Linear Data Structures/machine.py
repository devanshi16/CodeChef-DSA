#There are N boxes in a line (numbered 1 through N). Initially, the boxes are empty, and I need to use the machine to put tokens in them. 
# For each valid i,the i-th box has a maximum capacity Si tokens. I can perform the following operation any number of times: choose an integer 
# L(1≤L≤N) and put one token in each of the boxes 1,2,…,L .
#Can you help me calculate the maximum number of tokens that can be put in these boxes?

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    a = [min(s)] * len(s)
    for i in range(len(a)):
        if (s[i] > min(s)):
            a[i] += 1
        else:
            break
    print(sum(a))