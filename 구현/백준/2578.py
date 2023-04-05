import sys
input = sys.stdin.readline

board = []
numbers = []
for _ in range(5):
    board.append(list(map(int, input().split())))

for _ in range(5):
    numbers.extend(list(map(int, input().split())))


def check():
    bingo = 0
    cross_down = 0
    cross_up = 0

    for i in range(5):
        if board[i].count(0) == 5:
            bingo += 1

    for i in range(5):
        zero_num = 0
        for j in range(5):
            if board[j][i] == 0:
                zero_num += 1

        if zero_num == 5:
            bingo += 1

    for i in range(5):
        if board[i][i] == 0:
            cross_down += 1
        if board[4-i][i] == 0:
            cross_up += 1

    if cross_down == 5:
        bingo += 1

    if cross_up == 5:
        bingo += 1

    return bingo


cnt = 0
for num in numbers:
    for x in range(5):
        for y in range(5):
            if board[x][y] == num:
                board[x][y] = 0
                cnt += 1

    if cnt >= 12:
        if check() >= 3:
            print(cnt)
            break
