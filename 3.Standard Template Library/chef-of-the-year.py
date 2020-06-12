n, m = map(int,input().split())
chef_country = {}
for _ in range(n):
    chef,country=input().split()
    chef_country[chef]=country
freq = {}
freq_c = {}
for _ in range(m):
    ch=input()
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1    
    if chef_country[ch] in freq_c:
        freq_c[chef_country[ch]]=freq_c[chef_country[ch]]+1
    else:
        freq_c[chef_country[ch]]=1
freq_max=max(freq.values())
freq_cmax=max(freq_c.values())
ans_ch=[]
ans_co=[]
for k,v in chef_country.items():
    if freq.get(k,0)==freq_max:
        ans_ch.append(k)
    if freq_c.get(chef_country[k],0)==freq_cmax:
         ans_co.append(chef_country[k])
ans_co.sort()
ans_ch.sort()
print(ans_co[0])
print(ans_ch[0])