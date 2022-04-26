def read():
    clients = []
    t = int(input())
    for _ in range(t):
        client = []
        n = int(input().split()[0])
        for _ in range(n):
            client.append(list(map(int, input().split())))
        clients.append(client)

    return clients


def go(clients):
    ress = []

    for products in clients:
        res = 0
        current = [0]

        for product in products:

            minn, maxx = min(product), max(product)

            if len(current) == 1:
                dstup = abs(maxx - current[0])
                dstdown = abs(minn - current[0])

                if dstup > dstdown:
                    res += abs(current[0] - minn)
                    current = [maxx]
                elif dstup < dstdown:
                    res += abs(current[0] - maxx)
                    current = [minn]
                else:
                    res += abs(current[0] - maxx)
                    current = [minn, maxx]

            else:
                dstup1 = abs(maxx - current[0])
                dstdown1 = abs(minn - current[0])

                dstup2 = abs(maxx - current[1])
                dstdown2 = abs(minn - current[1])

                if min(dstup1, dstdown1) == min(dstup2, dstdown2):
                    res += min(dstdown1, dstup1, dstup2, dstdown2)
                    current = [minn, maxx]

                elif min(dstup1, dstdown1) < min(dstup2, dstdown2):
                    res += min(dstup1, dstdown1)
                    current = [minn]
                else:
                    res += min(dstup2, dstdown2)
                    current = [maxx]

            res += maxx - minn

            current = list(set(current))

        ress.append(res)

    return ress


def out(res):
    for i, r in enumerate(res):
        print(f'Case #{i+1}: {r}')


def main():
    numbers = read()
    res = go(numbers)
    out(res)


if __name__ == '__main__':
    main()
