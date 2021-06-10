N = int(input())
Z, W = [0]*N, [0]*N

for n in range(N):
    x, y = map(int, input().split())
    Z[n] = x+y
    W[n] = x-y

ans = max(max(Z)-min(Z), max(W)-min(W))
print(ans)