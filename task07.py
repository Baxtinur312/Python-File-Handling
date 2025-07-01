def task7():
    with open("numbers.txt") as f:
        numbers = list(map(int, f.read().split()))
    kvadratlar = [n**2 for n in numbers]
    return kvadratlar
