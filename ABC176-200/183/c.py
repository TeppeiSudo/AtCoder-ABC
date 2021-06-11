from itertools import permutations

N, K = map(int, input().split())
T = [[0]*(N+1) for _ in range(N+1)]

for n in range(1, N+1):
    T[n][1:] = list(map(int, input().split()))

cities = list(range(2, N+1))
ans = 0
for p in permutations(cities, N-1):
    time = T[1][p[0]] + T[p[-1]][1]
    for i in range(N-2):
        time += T[p[i]][p[i+1]]
    if time == K:
        ans += 1

print(ans)