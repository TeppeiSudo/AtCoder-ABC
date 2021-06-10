A, B, W = map(int, input().split())
W *= 1000

upper = W//A
lower = -(-W//B)

if lower > upper:
  print("UNSATISFIABLE")
else:
  print(lower,upper)