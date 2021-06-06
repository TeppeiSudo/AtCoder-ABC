import sys
sys.setrecursionlimit(500*500)

N, M = map(int, input().split())
A, B = [0]*(M+1), [0]*(M+1)
G = [[] for _ in range(N+1)]
for m in range(1, M+1):
    A[m], B[m] = map(int, input().split())
    G[A[m]].append(B[m])
  
def dfs(graph, start, goal):
    goal.add(start)
    for nex in graph[start]:
        if nex not in goal:
            goal = dfs(graph, nex, goal)
    return goal

ans = 0
for n in range(1, N+1):
    goal = dfs(G, n, set())
    ans += len(goal)
print(ans)