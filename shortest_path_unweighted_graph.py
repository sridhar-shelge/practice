def bfs_m(graph,s,d):
    visited=[False]*(len(graph))
    q=[s]
    visited[s]=True
    distance=[-1]*(len(graph))
    distance[s]=0
    while(q):
        t=q.pop(0)
        for i in graph[t]:
            if visited[i]==False:
                distance[i]=distance[t]+1
                visited[i]=True
                q.append(i)
    return distance[d]

n,m,t,c=map(int,input().split())
l=[]
for i in range(m):
    ab=list(map(int,input().split()))
    l.append(ab)
graph=[]
for i in range(n+1):
    graph.append([])

for i in range(len(l)):
    graph[l[i][0]].append(l[i][1])
    graph[l[i][1]].append(l[i][0])
ans=bfs_m(graph,1,n)

tim = 0
for i in range(ans):
    tim += c
    if i==ans-1:
        break
    else:
        temp = tim//t
        if temp%2==1:
            tim = (temp+1)*t

print(tim)


