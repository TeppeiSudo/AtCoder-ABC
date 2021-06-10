N, M = map(int, input().split())
A = [0]*(M+2)
A[-1] = N+1
if M:
    Am = list(map(int, input().split()))
    A[1:-1] = sorted(Am)

k = N
whites = []
for m in range(1, M+2):
    white = A[m]-A[m-1]-1
    if white > 0:
        whites.append(white)
        k = min(k, white)

ans = 0
for w in whites:
    ans += -(-w//k)
print(ans)