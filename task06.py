def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))

def task6():
    odds = [x for x in read_numbers() if x % 2 == 1]
    with open("odd_numbers.txt", "w") as f:
        for n in odds:
            f.write(str(n) + "\n")
    return odds
