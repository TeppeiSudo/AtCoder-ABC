N, K = map(int, input().split())
med = K**2//2+1

A = [[0]*N for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))

left = -1
right = 10**9+1
while left+1 < right:
    mid = (left+right)//2

    s = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j]
            if A[i][j] > mid:
                s[i+1][j+1] += 1

    ext = False
    for i in range(N-K+1):
        for j in range(N-K+1):
            if (s[i+K][j+K] + s[i][j] - s[i][j+K] -s[i+K][j]) < med:
                ext = True
                
    if ext:
        right = mid
    else:
        left = mid

print(right)