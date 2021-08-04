import math
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    ind=[]
    mini=math.inf
    for i in range(n):
        if (a[0]+b[i])%n<mini:
            ind=[]
            ind.append(i)
            mini=(a[0]+b[i])%n
        elif (a[0]+b[i])%n<=mini:
            ind.append(i)
   
    l=[]
    for i in ind:
        s=b[i:]+b[:i]
        x=[]
     
        for j in range(n):
            x.append((a[j]+s[j])%n)
      
        l.append(x)
    l.sort()
    print(*l[0])

    
            
            
        

    
    

    

