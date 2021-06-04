N = int(input())

def is_include7(number):
  ans = False
  for n in range(13):
  # 10*nの位が7かどうか
    if (number // 10**n) % 10 == 7:
      ans = True
      break
    if (number // 8**n) % 8 == 7:
      ans = True
      break
  return ans


count = 0
for n in range(1, N+1):
  if not is_include7(n):
    count += 1

print(count)