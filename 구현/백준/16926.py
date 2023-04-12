n, m, r = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

padding = 0
while True:
    if min(n, m) == 2 * padding:
        break

    start_col, end_col = padding, m - 1 - padding
    start_row, end_row = padding, n - 1 - padding
    tmp = []

    for j in range(end_col, start_col, -1):
        tmp.append(board[start_row][j])

    for i in range(start_row, end_row):
        tmp.append(board[i][start_col])

    for j in range(start_col, end_col):
        tmp.append(board[end_row][j])

    for i in range(end_row, start_row, -1):
        tmp.append(board[i][end_col])

    cut_idx = len(tmp) - r % len(tmp)

    tmp = tmp[cut_idx:] + tmp[:cut_idx]
    tmp.reverse()

    for j in range(end_col, start_col, -1):
        board[start_row][j] = tmp.pop()

    for i in range(start_row, end_row):
        board[i][start_col] = tmp.pop()

    for j in range(start_col, end_col):
        board[end_row][j] = tmp.pop()

    for i in range(end_row, start_row, -1):
        board[i][end_col] = tmp.pop()

    padding += 1

for line in board:
    print(*line)
