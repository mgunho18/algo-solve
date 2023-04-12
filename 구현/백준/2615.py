import sys

input = sys.stdin.readline
N = 19
board = []
dirs = [(1, 0), (0, 1), (1, 1), (-1, 1)]

for _ in range(N):
    board.append(list(map(int, input().split())))

for x in range(N):
    for y in range(N):
        cur = board[x][y]

        if cur == 0:
            continue

        for dx, dy in dirs:
            cnt = 1
            nx, ny = x, y

            while True:
                if cnt == 5:
                    if 0 <= x - dx < N and 0 <= y - dy < N:
                        if cur == board[x - dx][y - dy]:
                            break

                    if 0 <= nx + dx < N and 0 <= ny + dy < N:
                        if cur == board[nx + dx][ny + dy]:
                            break

                    print(cur)
                    print(x + 1, y + 1)
                    exit(0)

                nx += dx
                ny += dy

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break

                if cur == board[nx][ny]:
                    cnt += 1

                else:
                    break

print(0)
