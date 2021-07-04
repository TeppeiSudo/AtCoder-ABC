from heapq import heappop, heappush
from math import sqrt

N, M = map(int, input().split())
A, B, C, D = [0]*(M+1), [0]*(M+1), [0]*(M+1), [0]*(M+1)

E = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for m in range(1, M+1):
    A[m], B[m], C[m], D[m] = map(int, input().split())
    graph[A[m]].append(B[m])
    graph[B[m]].append(A[m])
    E[A[m]].append((C[m], D[m]))
    E[B[m]].append((C[m], D[m]))

def get_time(time, c, d):
    time0 = sqrt(d) - 1
    time1, time2 = int(time0)+1, int(time0)
    time1 = max(time, time1)
    time2 = max(time, time2)
    if time1+c+d//(time1+1) < time2+c+d//(time2+1):
        return time1-time+c+d//(time1+1)
    else:
        return time2-time+c+d//(time2+1)

start = 1
dist = [10**18]*(N+1)
dist[start] = 0
hque = [(dist[start], start)]
while hque:
    pos = heappop(hque)
    if pos[0] > dist[pos[1]]:
        continue
    pos = pos[1]
    for nex, cd in zip(graph[pos], E[pos]):
        c, d = cd
        cost = get_time(dist[pos], c, d)
        if dist[nex] > dist[pos] + cost:
            dist[nex] = dist[pos] + cost
            heappush(hque, (dist[nex], nex))

if dist[N] == 10**18:
    print(-1)
else:
    print(dist[N])