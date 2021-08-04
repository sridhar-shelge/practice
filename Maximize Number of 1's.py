#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    #brute
    ans=0
    for i in range(len(arr)):
        cnt=0
        temp=m
        for j in range(i,len(arr)):
            if(temp==0):
                while(j<len(arr) and arr[j]!=0):
                    cnt+=1
                    j+=1
                break
            if(arr[j]==1):
                cnt+=1
            else:
                temp-=1
                cnt+=1
        #print(cnt)
        ans=max(cnt,ans)
    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends
