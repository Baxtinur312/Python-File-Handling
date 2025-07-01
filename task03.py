def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))

def task3():
    return max(read_numbers())

