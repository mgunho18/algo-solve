target = list(input())
res = [""] * len(target)


def recursive(arr, start):
    if not arr:
        return

    min_val = min(arr)
    idx = arr.index(min_val)
    res[start + idx] = min_val
    print("".join(res))

    recursive(arr[idx + 1:], start + idx + 1)
    recursive(arr[:idx], start)


recursive(target, 0)
