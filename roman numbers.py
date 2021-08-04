#User function Template for python3



def romanToDecimal(str):
    # code here
    total=0
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    i=0
    if(len(str)==1):
        return d[str[0]]
    while(i<len(str)):
        if(i==len(str)-1):
            total+=d[str[i]]
        elif(d[str[i+1]]>d[str[i]]):
            total+=d[str[i+1]]-d[str[i]]
            i+=1
        else:
            total+=d[str[i]]
        i+=1
        
    return total

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        print(romanToDecimal(str(input())))
# } Driver Code Ends
