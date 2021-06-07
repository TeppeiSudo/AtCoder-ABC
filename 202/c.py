N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

candidate1 = [0]*(N)
candidate2 = [0]*(N)
for a, c in zip(A, C):
  candidate1[a-1] += 1
  candidate2[B[c-1]-1] += 1

ans = 0
for c1, c2 in zip(candidate1, candidate2):
  ans += c1*c2
  
print(ans)