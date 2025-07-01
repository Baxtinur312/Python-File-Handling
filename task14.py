with open("students.txt") as f:
    names = f.read().splitlines()
print("Teskari tartib:", list(reversed(names)))
