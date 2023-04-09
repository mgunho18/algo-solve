def solution(n, arr1, arr2):
    answer = []
    binary = []

    for i in range(n):
        res = bin(arr1[i] | arr2[i])[2:]
        tmp = []

        for i in range(len(res), 0, -1):
            tmp.append(res[i-1])

        for _ in range(n - len(res)):
            tmp.append(0)

        tmp.reverse()
        binary.append(''.join(map(str, tmp)))

    for each in binary:
        tmp = ''
        for i in range(n):
            if each[i] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer
