def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))


def task2():
    return sum(read_numbers())
