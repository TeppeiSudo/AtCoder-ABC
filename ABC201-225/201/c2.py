from itertools import product

def check(candidate, S):
    for i, s in enumerate(S):
        if s == "o":
            if i not in candidate:
                return False
        elif s == "x":
            if i in candidate:
                return False
    return True

S = str(input())
p = list(range(10))
ans = 0
for candidate in product(p, repeat=4):
    if check(candidate, S):
        ans += 1
print(ans)