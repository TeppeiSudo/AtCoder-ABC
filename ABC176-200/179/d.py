N, K = map(int, input().split())
L, R = [0]*K, [0]*K
S = [0]*K

for k in range(K):
    L[k], R[k] = map(int, input().split())
    S[k] = (L[k], R[k])

dp = [0]*(N+1)
dpsum = [0]*(N+1)
dp[1] = dpsum[1] = 1
for n  in range(2, N+1):
    for l, r in S:
        if n > l:
            r = min(n, r)
            dp[n] += dpsum[n-l] - dpsum[n-r-1]
    dpsum[n] = dpsum[n-1] + dp[n]
    dpsum[n] %= 998244353
    dp[n] %=998244353

print(dp[N])