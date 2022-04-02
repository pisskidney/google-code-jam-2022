def draw(r: int, c: int):

    def draw_horizontal(n: int):
        return ['+', '-'] * n + ['+']

    def draw_vals(n: int):
        return ['|', '.'] * n + ['|']

    res = []
    for _ in range(r):
        res.append(draw_horizontal(c))
        res.append(draw_vals(c))
    res.append(draw_horizontal(c))

    res[0][0] = '.'
    res[0][1] = '.'
    res[1][0] = '.'

    return [''.join(x) for x in res]


def go():
    t = input()
    inputs = []
    for _ in range(int(t)):
        r, c = map(int, input().split(' '))
        inputs.append([r, c])

    for i, inputt in enumerate(inputs):
        r, c = inputt
        print(f'Case #{i+1}:')
        res = draw(r, c)
        for row in res:
            print(row)


def main():
    go()


if __name__ == '__main__':
    main()
