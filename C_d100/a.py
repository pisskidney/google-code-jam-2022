from typing import List


def get_longest(die: List[int]) -> int:
    index = 1
    for i, nr in enumerate(sorted(die)):
        if nr < index:
            continue
        else:
            index += 1
    return index - 1


def go():
    t = input()
    inputs = []
    for _ in range(int(t)):
        _ = input()
        inputs.append(list(map(int, input().split(' '))))

    for i, inputt in enumerate(inputs):
        res = get_longest(inputt)
        print(
            f'Case #{i+1}: {str(res)}'
        )


def main():
    import time
    from random import shuffle
    start = time.monotonic()
    aaa = list(range(10**6))
    shuffle(aaa)
    print(get_longest(aaa))
    print(f'{time.monotonic() - start} seconds')


if __name__ == '__main__':
    main()
