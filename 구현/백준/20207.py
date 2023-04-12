import sys

input = sys.stdin.readline

N = int(input())
todo = [0] * 367  # E가 365까지 있는 경우 처리를 위해

for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S, E + 1):
        todo[i] += 1

tmp = []
ans = 0
for each in todo:
    if each == 0:
        if tmp:
            ans += len(tmp) * max(tmp)
            tmp = []
        continue
    else:
        tmp.append(each)

print(ans)
