N=4
arr=[1,4,3,2]
temp=0
flag=0
for i in range(N-1,0,-1):
    if(arr[i-1]<arr[i]):
        temp=i-1
        flag=1
        break
print(i)
if(flag==0):
    print(arr)
    #return arr[::-1]

pos=i
minn=arr[pos-1]
for j in range(pos+1,N):
    if(arr[j]<arr[pos] and arr[j]>minn):
        #minn=arr[j]
        temp=j
arr[pos-1],arr[temp]=arr[temp],arr[pos-1]
l=arr[pos:]
l.sort()
arr=arr[0:pos]+l
print(arr)
#return arr
        
