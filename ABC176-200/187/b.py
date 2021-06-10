N = int(input())
ans = 0
Z = [[] for _ in range(N)]
for n in range(N):
    Z[n] = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        xi, yi = Z[i]
        xj, yj = Z[j]
        if abs((yi-yj)/(xi-xj))<=1:
            ans += 1
print(ans)