from collections import namedtuple

N, STUDENT = int(input()), namedtuple('Student', input())

#extracts the MARKS from the namedTuple , sums them up and divides by N to get average
print("{:.2f}".format(sum([int(STUDENT(*input().split()).MARKS) for _ in range(N)]) / N))