import sys
input = sys.stdin.readline

n = int(input())
switch_list = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(1, n // num + 1):
            target = num * i - 1
            if switch_list[target]:
                switch_list[target] = 0
            else:
                switch_list[target] = 1

    elif sex == 2:
        base = num - 1
        span_max_length = min(base, n - 1 - base)
        available = 0

        for i in range(1, span_max_length + 1):
            if switch_list[base - i] == switch_list[base + i]:
                available = i
                continue
            else:
                break

        for j in range(base - available, base + available + 1):
            if switch_list[j]:
                switch_list[j] = 0
            else:
                switch_list[j] = 1

iter_num = n // 20

for i in range(iter_num):
    s, e = i * 20, (i+1) * 20
    print(*switch_list[s:e])

if n % 20:
    print(*switch_list[iter_num * 20:])
