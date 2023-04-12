from itertools import combinations


def holsu_cnt(num):
    val = 0
    for i in range(len(num)):
        if int(num[i]) % 2:
            val += 1

    return val


def cut_and_sum(num, prev_cnt):
    global candid

    if len(num) == 1:
        if int(num) % 2:
            candid.append(prev_cnt + 1)
        else:
            candid.append(prev_cnt)
        return

    if len(num) >= 3:
        prev_cnt += holsu_cnt(num)
        for a, b in combinations(range(1, len(num)), 2):
            tmp = int(num[:a]) + int(num[a:b]) + int(num[b:])
            cut_and_sum(str(tmp), prev_cnt)

    else:
        prev_cnt += holsu_cnt(num)
        tmp = int(num[0]) + int(num[1])
        cut_and_sum(str(tmp), prev_cnt)


N = input()
candid = []

cut_and_sum(N, 0)
candid.sort()
print(candid[0], candid[-1])
