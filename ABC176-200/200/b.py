N, K = map(int, input().split())
ans = [N]*K

for k in range(K):
    if N%200 == 0:
        N /= 200
    else:
        N *= 1000
        N += 200
print(int(N))