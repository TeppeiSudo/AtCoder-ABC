N = int(input())
X = N*1.08//1

if X < 206:
    ans = "Yay!"
elif X == 206:
    ans = "so-so"
else:
    ans = ":("
print(ans)