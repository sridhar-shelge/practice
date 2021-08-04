def DFS(g, visited, u, ar, ans, ans_ar, s):
    visited[u] = True
    
    ar[ord(s[u-1])-97] +=1
    
    
    for i in g[u]:
        if visited[i]==False:
            DFS(g, visited, i, ar, ans, ans_ar, s)
            
    ans_ar.append(max(ar))       
    ar[ord(s[u-1])-97] -=1
    
    
def isCycle(g, s, visited, recSta):
    visited[s] = True
    recSta[s] = True
    
    for e in g[s]:
        
        if visited[e]==False:
            if isCycle(g, e, visited, recSta):
                return True
            
        elif recSta[e] == True:
            return True
        
    recSta[s] = False
    return False
    


n,m = map(int, input().split())

s = input()
g = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int, input().split())
    g[u].append(v)
    
visited = [False]*(n+1)
recSta = [False]*(n+1)
flag = 0

for i in range(1,n+1):
    if visited[i]==False:
        if(isCycle(g,i, visited, recSta)):
            flag = 1
            print(-1)
            break

if flag ==0:
    visited = [False]*(n+1)
    t = 0
    for i in range(1,n+1):
        if visited[i]==False:
            ar = [0]*(26)
    
            ans_ar = []
            DFS(g, visited, 1, ar, 0, ans_ar, s)
            t = max(t, max(ans_ar))
            
    print(t)
