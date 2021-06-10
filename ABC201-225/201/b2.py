N = int(input())
S = [0]*N
T = [0]*N
D = {}

for n in range(N):
  S[n], T[n] = map(str, input().split())
  T[n] = int(T[n])
  D[T[n]] = S[n]

T.sort(reverse=True)
print(D[T[1]])