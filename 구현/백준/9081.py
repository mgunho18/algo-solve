def next_permutation(target):
    i = len(target) - 2
    while i >= 0 and target[i] >= target[i+1]:
        i -= 1
    if i == -1:
        return target

    j = len(target) - 1

    while target[i] >= target[j]:
        j -= 1

    target[i], target[j] = target[j], target[i]
    result = target[:i+1]
    result.extend(reversed(target[i+1:]))

    return result


n = int(input())

for _ in range(n):
    target = list(input())
    answer = next_permutation(target)
    print("".join(answer))
