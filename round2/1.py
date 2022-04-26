from collections import deque


def read():
    numbers = []
    t = int(input())
    for _ in range(t):
        _ = input()
        numbers.append(deque(list(map(int, input().split()))))
    return numbers


def go(numbers):

    res = []
    for nums in numbers:

        i = 0
        minn = -1

        while nums:

            if nums[0] <= nums[-1]:
                out = nums.popleft()
            else:
                out = nums.pop()

            if minn <= out:
                i += 1

            minn = max(minn, out)

        res.append(i)

    return res


def out(res):
    for i, r in enumerate(res):
        print(f'Case #{i+1}: {r}')

def main():
    numbers = read()
    res = go(numbers)
    out(res)


if __name__ == '__main__':
    main()
