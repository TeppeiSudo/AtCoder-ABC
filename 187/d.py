N = int(input())
A, B, C = [0]*N, [0]*N, [0]*N
for n in range(N):
    A[n], B[n] = map(int, input().split())
    C[n] = 2*A[n] + B[n]

C.sort(reverse=True)
diff = sum(A)
count = ans = 0
while count <= diff:
    count += C[ans]
    ans += 1
print(ans)