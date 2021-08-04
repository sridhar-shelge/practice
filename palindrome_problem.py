#User function Template for python3

class Solution:
    def nextPalin(self,N):
        #code here
        if(len(N)==1):
            return -1
        n=len(N)//2
        x=N[0:n]
        l=[i for i in x]
        for i in range(len(l)-1,-1,-1):
            if(l[i]>l[i-1]):
                #l[i],l[i-1]=l[i-1],[i]
                break
        
        pos=i-1
        minn=l[pos+1]
        temp=pos+1
        for i in range(pos+2,len(l)):
            if(l[i]<minn):
                temp=i
                minn=l[i]
        l[pos],l[temp]=l[temp],l[pos]
        #print(l)
        temp=sorted(l[pos+1:])
        l=l[:pos+1]+temp[::]
        #print(l)
        
        
        if(len(N)%2==0):
            ans=''.join(l)
            ans+=ans[::-1]
            if(int(ans)>int(N)):
                return ans
            return -1
        else:
            ans=''.join(l)
            ans+=N[n]+ans[::-1]
            if(int(ans)>int(N)):
                return ans
            return -1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
# } Driver Code Ends
