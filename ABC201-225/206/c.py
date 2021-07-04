from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

ans = N*(N-1)//2

counter = defaultdict(int)
for a in A:
    if counter[a]:
        ans -= counter[a]
    counter[a] += 1

print(ans)