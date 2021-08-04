#User function Template for python3


class Solution:
    
    def solve(self,graph,visited,s):
        visited[s]=True
        for i in graph[s]:
            if visited[i]==False:
                if self.solve(graph,visited,i):
                    return True
                
            elif(visited[i]==True):
                return True
        visited[s]=False
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited=[False]*(len(adj))
        for i in range(V):
            if visited[i]==False:
                if self.solve(adj,visited,i):
                    return 1
        return 0
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
