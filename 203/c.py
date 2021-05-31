N, K = map(int, input().split())

C = [0]*N
for n in range(N):
    C[n] = map(int, input().split())
  
pos = 0
for c in C:
    a, b = c
    if (a-pos) <= K:
        K += b
        K -= (a - pos)
        pos = a
    else:
        pos += K
        K = 0
        break
pos += K
print(pos)