def lower_bound(A, target):
    left = -1
    right = len(A)
    while left+1 <  right:
        mid = (left + right)//2
        if A[mid] >= target:
            right = mid
        else:
            left = mid
    return right

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
U, D = [0]*Q, [0]*Q
for q in range(Q):
    U[q], D[q] = map(int, input().split())

graph = [[] for _ in range(N+1)]
for n in range(N-1):
    graph[P[n]].append(n+2)

v = [[] for _ in range(N+1)]
dist = [0]*(N+1)
tin, tout = [0]*(N+1), [0]*(N+1)
def dfs(graph, start, counter):
    tin[start] = counter
    counter += 1
    v[dist[start]].append(counter)
    for nex in graph[start]:
        dist[nex] = dist[start] + 1
        counter = dfs(graph, nex, counter)
    tout[start] = counter
    counter += 1
    return counter

def solve(u, d):
    u -= 1
    A = v[d]
    return lower_bound(A, tout[u]) - lower_bound(A, tin[u])

dfs(graph, 1, 0)
for q in range(Q):
    u, d = U[q], D[q]
    print(solve(u, d))