import random


def main():
    nr_of_cases = int(input())

    for case in range(nr_of_cases):
        nr_of_rooms, nr_of_tries = map(int, input().split())
        room_number, nr_of_passages = map(int, input().split())

        all_passages = 0

        if nr_of_tries > nr_of_rooms:
            nr_of_tries = nr_of_rooms
        random_tries = list(range(1, nr_of_rooms + 1))
        random.shuffle(random_tries)
        random_tries = random_tries[:nr_of_tries-1]

        for i in random_tries:
            print('T ' + str(i), flush=True)
            room_number, nr_of_passages = map(int, input().split())
            all_passages += nr_of_passages

        if nr_of_rooms <= nr_of_tries:
            m = int(all_passages / 2)
        else:
            n = nr_of_rooms - nr_of_tries
            m = int(all_passages / 2) + ((n * all_passages / nr_of_tries) / 2)

        print('E ' + str(int(m)), flush=True)


main()
