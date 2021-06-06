N = int(input())
T = list(map(int, input().split()))

dp = [[False]*(N+1) for _ in range(10**5+1)]
for n in range(N+1):
    dp[0][n] = True

for i in range(1, 10**5+1):
    for n in range(N+1):
        dp[i][n] = dp[i][n-1]
        if (n>0)and(i >= T[n-1]):
            dp[i][n] = dp[i][n] or dp[i-T[n-1]][n-1]

sumT = sum(T)
for i in range(-(-sumT//2), 10**5+1):
    if dp[i][N]:
        print(i)
        break