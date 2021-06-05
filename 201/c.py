from itertools import product
S = str(input())
C = []
U = []

for i, s in enumerate(S):
  if s == "o":
    C.append(i)
    U.append(i)
  elif s == "?":
    U.append(i)
    
def check(candidate, C):
  for c in C:
    if c not in candidate:
      return False
  return True
    
count = 0
for candidate in product(U, repeat=4):
  if check(candidate, C):
      count += 1
print(count)