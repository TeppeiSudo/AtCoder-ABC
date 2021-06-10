N = int(input())
S = [""]*(N+1)
for n in range(1,N+1):
    S[n] = str(input())

dp = [0]*(N+1)
dp[0] = 1
for n in range(1, N+1):
    if S[n] == "AND":
        dp[n] = dp[n-1]
    else:
        dp[n] = dp[n-1] + 2**n

print(dp[N])