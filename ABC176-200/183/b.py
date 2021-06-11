sx, sy, gx, gy = map(int, input().split())
gy *= -1

ans = -sy/((gy-sy)/(gx-sx)) + sx
print(ans)