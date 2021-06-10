A, B = map(str, input().split())
sa = sb = 0
for i in range(3):
    sa += int(A[i])
    sb += int(B[i])
print(max(sa, sb))