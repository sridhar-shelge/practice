# cook your dish here
import sys
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in range(len(l)):
        ans+=n-d[l[i]]-i
        d[l[i]]-=1
    print(ans*2)
