N = int(input())
S = set()
for n in range(N):
    S.add(str(input()))

ans = "satisfiable"
for s in S:
    if "!"+s in S:
        ans = s
        break
print(ans)