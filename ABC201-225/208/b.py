P = int(input())

coins = [0]
coin = 1
for i in range(1, 11):
  coin *= i
  coins.append(coin)
  
ans = 0
for n in range(10, 0, -1):
  if coins[n] <= P:
    ans += P//coins[n]
    P %= coins[n]
print(ans)