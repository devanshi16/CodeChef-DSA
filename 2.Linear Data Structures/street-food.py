#in Chefland, there is a very famous street where N types of street food (numbered 1 through N) are offered. For each valid i, there are Si stores that offer food of the i-th type, the price of one piece of food of this type is Vi
# (the same in each of these stores) and each day, Pi people come to buy it; each of these people wants to buy one piece of food of the i-th type.

#Chef is planning to open a new store at this street, where he would offer food of one of these N
# types. Chef assumes that the people who want to buy the type of food he'd offer will split equally among all stores that offer it, and if this is impossible, i.e. the number of these people p
#is not divisible by the number of these stores s, then only ⌊ps⌋ people will buy food from Chef.

#Chef wants to maximise his daily profit.
t = int(input())
for _ in range(t):
    n = int(input())
    profit = []
    for i in range(n):
        s, p, v = input().split()
        s, p, v = int(s), int(p), int(v)
        profit.append((p//(s+1))*v)
    print(max(profit))