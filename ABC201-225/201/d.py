H, W = map(int, input().split())
A = [""]*H
for h in range(H):
    A[h] = str(input())

inf = 4000001
dp = [[0]*(W) for _ in range(H)]
for h in range(H):
    for w in range(W):
        dp[h][w] = -inf if (h+w)%2 == 0 else inf
dp[H-1][W-1] = 0

for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        if (h+w)%2==0:
            if h < H-1:
                dp[h][w] = max(dp[h][w], dp[h+1][w]+1 if A[h+1][w]=="+" else dp[h+1][w]-1)
            if w < W-1:
                dp[h][w] = max(dp[h][w], dp[h][w+1]+1 if A[h][w+1]=="+" else dp[h][w+1]-1)
        else:
            if h < H-1:
                dp[h][w] = min(dp[h][w], dp[h+1][w]-1 if A[h+1][w]=="+" else dp[h+1][w]+1)
            if w < W-1:
                dp[h][w] = min(dp[h][w], dp[h][w+1]-1 if A[h][w+1]=="+" else dp[h][w+1]+1)
            
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] == 0:
    print("Draw")
else:
    print("Aoki")