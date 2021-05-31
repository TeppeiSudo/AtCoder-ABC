N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

inf = 10**9+1
# 10**9 < 16**9 = 2**36
dp = [[inf]*38 for _ in range(N+3)]
# dp["草の数"]["高橋"] = "青木"

def upper_bound(A, target):
    left = -1
    right = len(A)
    while left+1 <  right:
        mid = (left + right)//2
        if A[mid] >= target:
            right = mid
        else:
            left = mid
    return left

dp[0][0] = 0
for i in range(N):
    for t in range(37):
        if dp[i][t] != inf:
            dp[i+1][t] = min(dp[i+1][t], dp[i][t]+1)
            nex = upper_bound(A, A[i]*2) + 1
            dp[nex][t+1] = min(dp[nex][t+1], dp[i][t])

for t in range(37):
    if dp[N][t] <= K:
        print(t, dp[N][t])
        break