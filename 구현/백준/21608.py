N = int(input())
seats = [[-1] * N for _ in range(N)]
change = [(-1, 0), (1, 0), (0, 1), (0, -1)]
score = 0
stdFrdDict = dict()

for _ in range(N * N):
    nums = input().split(' ')
    std = nums[0]
    frds = nums[1:]
    stdFrdDict[std] = frds
    seatConDict = dict()

    for x in range(N):
        for y in range(N):
            if seats[x][y] != -1:
                continue

            nearFrds, blank = 0, 0

            for dx, dy in change:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if seats[nx][ny] in frds:
                        nearFrds += 1
                    elif seats[nx][ny] == -1:
                        blank += 1
                else:
                    continue

            seatConDict[(x, y)] = (nearFrds, blank, x, y)

    fx, fy = sorted(seatConDict.values(), key=lambda k: (-k[0], -k[1], k[2], k[3]))[0][2:]
    seats[fx][fy] = std

for x in range(N):
    for y in range(N):
        nearFrds = 0
        frds = stdFrdDict[seats[x][y]]
        for dx, dy in change:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if seats[nx][ny] in frds:
                    nearFrds += 1
            else:
                continue
        if nearFrds:
            score += 10 ** (nearFrds - 1)

print(score)
