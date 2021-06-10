N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    x = A[l]
    for r in range(l, N):
        x = min(x, A[r])
        candidate = (r-l+1)*x
        ans = max(ans, candidate)

print(ans)