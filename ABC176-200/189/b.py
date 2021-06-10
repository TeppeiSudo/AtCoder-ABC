N, X = map(int, input().split())

ans = -1
alc = 0
for n in range(N):
    v, p = map(int, input().split())
    alc += v*p
    if alc > 100*X:
        ans = n +1
        break
print(ans)