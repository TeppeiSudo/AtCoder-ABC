A, B, C, D = map(int, input().split())

if C*D > B:
  print(-(-A//(C*D-B)))
else:
  print(-1)