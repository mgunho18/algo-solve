k = int(input())
n = int(input())
final = list(input())
start = sorted(final)
before_blur = []
after_blur = []
lines = []

for _ in range(n):
    lines.append(list(input()))

for idx, line in enumerate(lines):
    if line[0] == '?':
        before_blur.extend(lines[:idx])
        after_blur.extend(lines[idx + 1:])
        break

for line in before_blur:
    for i in range(k-1):
        if line[i] == '-':
            start[i], start[i+1] = start[i+1], start[i]

after_blur.reverse()
for line in after_blur:
    for i in range(k-1):
        if line[i] == '-':
            final[i], final[i+1] = final[i+1], final[i]

answer = ['*' for _ in range(1, k)]
for i in range(k-1):
    if start[i] == final[i+1] and start[i+1] == final[i]:
        answer[i] = '-'
        start[i], start[i+1] = start[i+1], start[i]

is_same = True

for i in range(k):
    if start[i] != final[i]:
        is_same = False
        break

if is_same:
    print(''.join(answer))
else:
    ans = 'x' * (k-1)
    print(ans)
