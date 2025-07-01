with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
print("1️ Barcha sonlar:", numbers)
