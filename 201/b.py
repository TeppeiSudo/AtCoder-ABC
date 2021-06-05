N = int(input())
S = [0]*N
T = [0]*N

t1 = 0
t2 = 0
s1 = ""
s2 = ""

for n in range(N):
  S[n], T[n] = map(str, input().split())
  T[n] = int(T[n])
  if t1 < T[n]:
    if t2 < t1:
      t2 = t1
      s2 = s1
    t1 = T[n]
    s1 = S[n]
  elif t2 < T[n]:
    t2 = T[n]
    s2 = S[n]
print(s2)
