import sympy
from functools import *
from math import *
from collections import *
prime = list(sympy.primerange(1,102))
for _ in range(int(input().strip())):
    n=int(input().strip())
    l=list(map(int,input().strip().split()))
    ans1=0
    for i in range(1,n):
        if(l[i]<l[i-1]):
            ans1+=l[i-1]-l[i]
            l[i]+=(l[i-1]-l[i])
    gc=reduce(gcd,l)
    if(gc!=1):
        print(ans1)
        continue
    else:
        ans=10**6
        for i in range(len(prime)):
            x=0
            for j in range(n):
                y=l[j]%prime[i]
                if(y!=0):
                    x+=(prime[i]-y)
            ans=min(ans,x)
        print(ans+ans1)