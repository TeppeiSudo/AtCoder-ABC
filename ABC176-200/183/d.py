N, W = map(int, input().split())
A = [0]*(2*10**5+2)

for n in range(N):
    s, t, p = map(int, input().split())
    A[s] += p
    A[t] -= p

sumA = [0]*(2*10**5+1)
for i, a in enumerate(sumA):
    sumA[i] = sumA[i-1] + A[i]

if max(sumA) <= W:
    ans = "Yes"
else:
    ans = "No"
print(ans)