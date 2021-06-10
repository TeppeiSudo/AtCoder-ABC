A = list(map(int, input().split()))

sA = sorted(A)
if sA[2]-sA[1] == sA[1]-sA[0]:
  print("Yes")
else:
  print("No")