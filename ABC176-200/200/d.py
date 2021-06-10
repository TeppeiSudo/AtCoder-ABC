from itertools import combinations, combinations_with_replacement

N = int(input())
A = list(map(int, input().split()))
Amod = A + [0]

for i, a in enumerate(A):
  Amod[i+1] = a%200
  
index = list(range(1,N+1))
def main():
    for b, c in combinations_with_replacement(index, 2):
        for B in combinations(index, b):
            for C in combinations(index, c):
                if (B != C) and (sum([Amod[Bidx] for Bidx in B])%200 == sum([Amod[Cidx] for Cidx in C])%200):
                    print("yes")
                    print(len(B), *B)
                    print(len(C), *C)
                    return
    print("No")
    return
    
main()