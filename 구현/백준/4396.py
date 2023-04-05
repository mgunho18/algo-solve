import sys
input = sys.stdin.readline

n = int(input())
board = []
actions = []
bombs = []
result = [['.'] * n for _ in range(n)]
exploded = False

for i in range(n):
    board.append(input())
    for idx, elem in enumerate(board[i]):
        if elem == '*':
            bombs.append((i, idx))

for _ in range(n):
    actions.append(input())


def count_bombs(x, y):
    cnt = 0
    change = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in change:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == '*':
                cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        if actions[i][j] == 'x':
            if board[i][j] == '.':
                result[i][j] = str(count_bombs(i, j))
            else:
                if not exploded:
                    for x, y in bombs:
                        result[x][y] = '*'
                    exploded = True

for line in result:
    print(*line, sep='')
