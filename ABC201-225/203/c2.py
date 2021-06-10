N, K = map(int, input().split())

C = [0]*N
for n in range(N):
    a, b = map(int, input().split())
    C[n] = a, b

C.sort()
for c in C:
    a, b = c
    if a <= K:
        K += b
    else:
        break
print(K)