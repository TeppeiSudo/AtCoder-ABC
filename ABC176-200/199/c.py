N = int(input())
S = str(input())
Q = int(input())

listS = [s for s in S]
flip = 0
for q in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1

    if t == 1:
        if flip%2 == 0:
            listS[a], listS[b] = listS[b], listS[a]
        else:
            listS[a-N], listS[b-N] = listS[b-N], listS[a-N]

    elif t == 2:
        flip += 1
    
if flip%2 != 0:
    listS = listS[N:] + listS[:N]
print("".join(listS))