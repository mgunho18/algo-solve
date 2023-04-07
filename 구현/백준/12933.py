target = input()
ducks = []
ans = 0

for char in target:
    valid = False
    if char == 'q':
        ducks.append([c for c in "uack"])
    else:
        for duck in ducks:
            if char == duck[0]:
                valid = True
                del duck[0]

                if not duck:
                    ducks.remove(duck)

                break
            else:
                continue

        if not valid:
            print(-1)
            exit(0)

    ans = max(ans, len(ducks))

if not ducks:
    print(ans)
else:
    print(-1)
