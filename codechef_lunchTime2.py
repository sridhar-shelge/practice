# cook your dish here
def solve(a,b,i1,i2,n):
    start=i1
    end=i2
    i=0
    mod1=(a[i]+b[i1])%n
    mod2=(a[i]+b[i2])%n
    while(i<n and mod1==mod2):
        i1=(i1+1)%n
        i2=(i2+1)%n
        i+=1
        mod1=(a[i]+b[i1])%n
        mod2=(a[i]+b[i2])%n
    if(mod1<mod2):
        return start
    return end

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    index=[]
    temp=[]
    for i in range(len(b)):
        temp.append((a[0]+b[i])%n)
    minn=min(temp)
    for i in range(len(temp)):
        if(temp[i]==minn):
            index.append(i)
    rotate=index[0]
    #print(index)
    if(len(index)==2):
        rotate=solve(a,b,index[0],index[1],n)
        
    for i in range(rotate):
        b.append(b.pop(0))
    c=[]
    for i in range(n):
        c.append((a[i]+b[i])%n)
    print(*c)
