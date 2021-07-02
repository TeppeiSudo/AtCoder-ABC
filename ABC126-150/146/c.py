A, B, X = map(int, input().split())

left = -1
right = 10**9+1
while left+1 <  right:
    mid = (left + right)//2
    d_mid = len(str(mid))
    if X < A*mid+B*d_mid:
        right = mid
    else:
        left = mid
ans= right-1
if ans == -1:
    ans = 0
print(ans)