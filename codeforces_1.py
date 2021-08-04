x=int(input())
y=list(map(int,input().split()))
z=list(map(int,input().split()))
temp=max=0
for i in range(0,x):
    max=temp
    for j in range(0,x):
        temp1=(y[i])**2
        temp2=(z[j])**2
        temp=temp1-temp2
        if(temp<0):
            temp=temp2-temp1
        if(temp>max):
            max=temp
print(max)
    
