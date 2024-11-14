import itertools

S = input().split()
STRING, NUMBER = sorted(S[0]), int(S[1])

print(*list(map(''.join, itertools.permutations(STRING, NUMBER))), sep='\n')


#code for combinations
"""
from itertools import combinations

S, N = input().split()

for i in range(1, int(N)+1):
    for j in combinations(sorted(S), i):
        print(''.join(j))
"""