def reverse_word(x):
    reversed_word = []
    for elem in x.split():
        reversed_word.append(''.join(reversed(elem)))

    return ' '.join(reversed_word)


target = input()
inBracket = False
ans = ''
tmp = ''
start, end = 0, 0
for idx, char in enumerate(target):
    if char == '<':
        start = idx
        ans += reverse_word(tmp)
        tmp = ''
        inBracket = True

    elif char == '>':
        end = idx
        ans += target[start:end+1]
        inBracket = False

    else:
        if not inBracket:
            tmp += char

if tmp:
    ans += reverse_word(tmp)

print(ans)
