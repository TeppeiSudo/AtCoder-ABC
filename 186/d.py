N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
for n in range(N-1):
    ans += A[n]*(N-n-1) - A[n+1]*(n+1)

print(ans)