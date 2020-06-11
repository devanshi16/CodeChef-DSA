#Pain has a strength of Z and is confident that he will succeed. Naruto has N
#soldiers under his command numbered 1 through N. Power of i-th soldier is denoted by Ai. 
# When a soldier attacks pain, his strength gets reduced by the corresponding power of the soldier. 
# However, every action has a reaction so the power of the soldier also gets halved i.e. Ai changes to [Ai/2]. 
# Each soldier may attack any number of times (including 0). Pain is defeated if his strength is reduced to 0 or less.
# Find the minimum number of times the soldiers need to attack so that the village is saved.
t = int(input())
for _ in range(t):
    n, z = input().split()
    n, z = int(n), int(z)
    a = [int(x) for x in input().split()]
    count = s = 0
    x=[]
    for i in a :
        while (i>0) :
            x.append(i)
            i = i//2
    x.sort(reverse = True)
    for i in x:
        z -= i
        count += 1
        if z <= 0:
            print(count)
            s = 1
            break
    if s == 0:
        print("Evacuate")