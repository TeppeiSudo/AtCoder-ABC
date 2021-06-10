N, X, M = map(int, input().split())

A = [0]*(M+1)
A[0] = -1
A[1] = X
used = set()
l, r = 1, N+1

for m in range(2, M+1):
    A[m] = (A[m-1]**2)%M
    if not A[m] in used:
        used.add(A[m])
    else:
        r = m
        l = A.index(A[m])
        break

ans = sum(A[1:l]) + (N-l)//(r-l)*sum(A[l:r]) + sum(A[l:l+(N-l)%(r-l)+1])
print(ans)