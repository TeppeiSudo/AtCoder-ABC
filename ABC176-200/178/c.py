N = int(input())
mod = 10**9+7

full = 10**N%mod
without0 = 9**N%mod
without9 = 9**N%mod
without09 = 8**N%mod

ans = full - without0 - without9 + without09
print(ans%mod)