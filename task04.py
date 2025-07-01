def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))

def task4():
    return [x for x in read_numbers() if x % 2 == 0]

