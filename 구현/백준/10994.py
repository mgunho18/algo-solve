def draw(n, idx):
    if n == 1:
        star_map[idx][idx] = '*'
        return

    l = 4 * n - 3

    for i in range(idx, l + idx):
        star_map[idx][i] = '*'
        star_map[idx + l - 1][i] = '*'

        star_map[i][idx] = '*'
        star_map[i][idx + l - 1] = '*'

    return draw(n - 1, idx + 2)


n = int(input())
length = 4 * n - 3

star_map = [[' '] * length for _ in range(length)]
draw(n, 0)

for line in star_map:
    print(*line, sep='')
