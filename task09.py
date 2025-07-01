def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))

def task9():
    return [(x, len(str(abs(x)))) for x in read_numbers()]
