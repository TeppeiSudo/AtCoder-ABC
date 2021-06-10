S = str(input())

rS = reversed(S)
ans = ""
for s in rS:
  if s == "6":
    ans += "9"
  elif s == "9":
    ans += "6"
  else:
    ans += s
    
print(ans)