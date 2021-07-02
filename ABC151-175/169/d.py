from math import sqrt
N = int(input())

def sieve(N):
    data = []
    for d in range(2, int(sqrt(N))+1):
        e = 0
        while N%d == 0:
            N //= d
            e += 1
        if e:
            data.append((d,e))
    if N>1:
        data.append((N,1))
    return data

ans = 0
for p, e in sieve(N):
    a = 1
    while a<=e:
        e -= a
        a += 1
        ans += 1
print(ans)