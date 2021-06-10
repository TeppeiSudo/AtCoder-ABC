H, W = map(int, input().split())
A = [[0 for i in range(W)] for j in range(H)]
min_A = 100

for i in range(H):
    A[i] = list(map(int, input().split()))
    min_A_i = min(A[i])
    min_A = min(min_A, min_A_i)

sum_ = 0
for i in range(H):
  for j in range(W):
    sum_ += A[i][j] - min_A
  
  
print(sum_)