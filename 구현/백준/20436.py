L, R = input().split()
target = input()
X = [0] * 26
Y = [0] * 26
onlyLeft = set()
ans = 0

for char in "qwertasdfgzxcv":
    onlyLeft.add(char)

tmp = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
for i, elem in enumerate(tmp):
    for j, char in enumerate(elem):
        idx = ord(char) - ord('a')
        X[idx], Y[idx] = i, j

L_idx = ord(L) - ord('a')
R_idx = ord(R) - ord('a')

for char in target:
    idx = ord(char) - ord('a')
    if char in onlyLeft:
        ans += abs(X[idx] - X[L_idx]) + abs(Y[idx] - Y[L_idx])
        ans += 1
        L_idx = idx
    else:
        ans += abs(X[idx] - X[R_idx]) + abs(Y[idx] - Y[R_idx])
        ans += 1
        R_idx = idx

print(ans)
