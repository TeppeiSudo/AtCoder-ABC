N, M = map(int, input().split())
I = [0]*M
for m in range(M):
    a, b = map(int, input().split())
    I[m] = a, b
K = int(input())
C, D = [0]*K, [0]*K
for k in range(K):
    C[k], D[k] = map(int, input().split())


ans = 0
for i in range(2**K):
    dishies = [0]*(N+1)

    # 皿にボールをおいていく
    for k in range(K):
        if (i>>k)&1:
            dishies[C[k]] = 1
        else:
            dishies[D[k]] = 1

    # 満たされている条件を数える
    count = 0
    for m in range(M):
        a, b = I[m]
        if (dishies[a] == 1)and(dishies[b] == 1):
            count += 1
    ans = max(ans, count)

print(ans)