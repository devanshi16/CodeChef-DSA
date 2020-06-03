#You are developing a smartphone app. You have a list of potential customers for your app. Each customer has a budget and will buy the app at your declared price if and only if the price is less than or equal to the customer's budget.You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.
n = int(input())
budget = []

for _ in range(n):
    budget.append(int(input()))
budget.sort()
maxr = 0
for i in range(n):
    revenue = budget[i]*(n-i)
    if revenue > maxr:
        maxr = revenue 
print(maxr)