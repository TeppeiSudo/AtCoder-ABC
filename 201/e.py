from collections import deque

N = int(input())
G = [[] for _ in range(N+1)]
W = [[] for _ in range(N+1)]
start = 1

for _ in range(N-1):
  u, v, w = map(int, input().split())
  G[u].append(v)
  G[v].append(u)
  W[u].append(w)
  W[v].append(w)

dist = [-1]*(N+1)
Q = deque([start])
dist[start] = 0
while Q:
    pos = Q.pop()
    for to, weight in zip(G[pos], W[pos]):
        if dist[to] == -1:
            dist[to] = dist[pos]^weight
            Q.append(to)

mod = int(1e9+7)
ans = 0
for i in range(60):
    cnt = [0]*2
    for j in range(N):
        cnt[dist[j+1]>>i&1] += 1
    ans += (1<<i)*cnt[0]*cnt[1]
    ans %= mod
print(ans)