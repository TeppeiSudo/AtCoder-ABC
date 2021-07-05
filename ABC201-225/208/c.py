N, K = map(int, input().split())
A = list(map(int, input().split()))
sA = list(sorted(A))

Ans = [K//N]*N
K %= N
border = sA[K-1]
if N == 1 or K == 0:
    border = -1

for ans, a in zip(Ans, A):
    if a <= border:
        print(ans + 1)
    else:
        print(ans)