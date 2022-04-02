def get_ink_levels(printers):

    limit = 10 ** 6

    mins = [limit + 1] * 4
    for printer in printers:
        for i in range(4):
            mins[i] = min(mins[i], printer[i])

    if sum(mins) < limit:
        return 'IMPOSSIBLE'

    total = 0
    res = []
    for nr in mins:
        if total + nr >= limit:
            res.append(limit - total)

            while len(res) < 4:
                res.append(0)

            break
        else:
            total += nr
            res.append(nr)

    return res


def go():
    t = input()
    inputs = []
    for _ in range(int(t)):
        row = []
        for _ in range(3):
            row.append(list(map(int, input().split(' '))))
        inputs.append(row)

    for i, inputt in enumerate(inputs):
        res = get_ink_levels(inputt)
        print(
            f'Case #{i+1}: {" ".join(list(map(str, res))) if res != "IMPOSSIBLE" else "IMPOSSIBLE"}'
        )


def main():
    go()


if __name__ == '__main__':
    main()
