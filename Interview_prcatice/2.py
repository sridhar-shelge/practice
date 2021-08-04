

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, graph):
        # Code here
        visited=[False]*(len(graph))
        in_degree=[0]*len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                in_degree[j]+=1
        #print(in_degree)
        ans=[]
        temp=in_degree.index(0)
        in_degree[temp]=-1
        q=[temp]
        while(q):
            t=q.pop(0)
            #print(t,'h')
            ans.append(t)
            for i in graph[t]:
                if visited[i]==False:
                    in_degree[i]-=1
                    if(in_degree[i]==0):
                        visited[i]=True
                        q.append(i)
            if(0 in in_degree):
                if(visited[in_degree.index(0)]==False):
                    temp=in_degree.index(0)
                    in_degree[temp]=-1
                    q.append(temp)
        print(ans)
        return ans
        

#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
