def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extgcd(b, a%b)
        return g, y, x-a//b*y

def solve(n, s, k):
    g, x, y = extgcd(k, n)
    if s%g != 0:
        return -1
    else:
        n //= g
        s //= g
        k //= g
        return ((x* -s)%n+n)%n
            
T = int(input())
for t in range(T):
    n, s, k = map(int, input().split())
    print(solve(n, s, k))