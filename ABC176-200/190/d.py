N = int(input())
while N % 2 == 0:
    N //= 2

sq = int(N ** 0.5)
ans = 0
for i in range(1, sq+1):
    ans += 1 if N%i==0 else 0
ans *= 2
ans -= 1 if sq*sq == N else 0

print(ans * 2)