import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
A = list(map(int, input().split()))
counter = [0]*200

for i, a in enumerate(A):
    A[i] = a%200
    counter[A[i]] += 1
  
ans = 0
for c in counter:
    if c > 1:
        ans += comb(c,2)
      
print(ans)