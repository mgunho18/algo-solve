n, m = map(int, input().split())
trains = [[0] * 20 for _ in range(n)]

for _ in range(m):
    cmd = list(map(int, input().split()))
    train_num = cmd[1]

    if cmd[0] == 1:
        seat_num = cmd[2]
        trains[train_num - 1][seat_num - 1] = 1

    elif cmd[0] == 2:
        seat_num = cmd[2]
        trains[train_num - 1][seat_num - 1] = 0

    elif cmd[0] == 3:
        trains[train_num - 1] = [0] + trains[train_num - 1][:-1]

    else:
        trains[train_num - 1] = trains[train_num - 1][1:] + [0]

ans = set()
for train in trains:
    ans.add(tuple(train))

print(len(ans))
