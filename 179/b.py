N = int(input())

count = 0
ans = "No"
for n in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        count += 1
        if count == 3:
            ans = "Yes"
            break
    else:
        count = 0
    
print(ans)