N = int(input())
T = [(0.0, 0.0) for _ in range(N)]

for n in range(N):
    t, r, l = map(int, input().split())
    if t == 1:
        T[n] = (r, l)
    elif t == 2:
        T[n] = (r, l-0.1)
    elif t == 3:
        T[n] = (r+0.1, l)
    elif t == 4:
        T[n] = (r+0.1, l-0.1)

def solve(a, b):
    if (min(T[a]) > max(T[b])) or (max(T[a]) < min(T[b])):
        ans = False
    else:
        ans = True
    return ans


ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += 1 if solve(i, j) else 0
print(ans)