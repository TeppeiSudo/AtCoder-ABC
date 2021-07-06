A, B, C = map(int, input().split())

ans = max(A+B, A+C, B+C)
print(ans)