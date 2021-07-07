N, Q = map(int, input().split())
S = str(input())

counter = [0]*(N)
for n in range(N-1):
    if S[n] == "A" and S[n+1] == "C":
        counter[n+1] += counter[n] + 1
    else: 
        counter[n+1] += counter[n]

for q in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(counter[r] - counter[l])