def subset(l,index,ans):
    if(index>=len(l)):
        print(ans)
        ans=[]
        return 
    subset(l,index+1,ans)
    ans+=str(l[index])
    subset(l,index+1,ans)

ans=''
l=[]
for i in range(5):
    l.append(i+1)
subset(l,0,ans)
