from collections import defaultdict

#n - no of strings to be added
#m - no of queries to be performed

N, M = map(int, input().split())
D = defaultdict(list)

for i in range(1, N + 1):
    D[input()].append(str(i))
for i in range(M):
    print(' '.join(D[input()]) or -1)