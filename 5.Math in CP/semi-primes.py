import sympy
prime = list(sympy.primerange(1,102))
sPrime = []
nums = []
for i in range(len(prime)):
    for j in range(i+1,len(prime)):
        sPrime.append(prime[i]*prime[j])
print(sPrime)
for i in range(len(sPrime)):
    for j in range(i,len(sPrime)):
        nums.append(sPrime[i]+sPrime[j])
for _ in range(int(input())):
    print("YES" if int(input()) in nums else "NO")