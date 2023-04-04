import sys

N, M = map(int, input().split())

bulbs = list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        bulbs[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if bulbs[i]:
                bulbs[i] = 0
            else:
                bulbs[i] = 1
    elif a == 3:
        for i in range(b-1, c):
            if bulbs[i]:
                bulbs[i] = 0
    else:
        for i in range(b-1, c):
            if not bulbs[i]:
                bulbs[i] = 1

print(*bulbs)