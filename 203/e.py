N, M = map(int, input().split())
blacks = [0]*M
for m in range(M):
    x, y = map(int, input().split())
    blacks[m] = (x, y)
  
blacks.sort()
blacks.append((-2,-2))  # 適当なtupleを入れてblacks[m]でout of rangeにならないようにする
road = set([N])
i = 0
while i < M:
    j = i + 1
    while blacks[i][0] == blacks[j][0]:
        j += 1

    tmp_add = set()
    tmp_rm = set()
    for k in range(i, j):
        x, y = blacks[k]
        if (y+1 in road) or (y-1 in road):
            tmp_add.add(y)
        elif y in road:
            tmp_rm.add(y)

    for a in tmp_add:
        road.add(a)
    for b in tmp_rm:
        road.remove(b)
    i = j
    
print(len(road))