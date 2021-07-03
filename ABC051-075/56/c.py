X = int(input())

for t in range(1, X+1):
    if t*(t+1)//2 >= X:
        print(t)
        break