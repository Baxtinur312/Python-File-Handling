with open("students.txt") as f:
    names = f.read().splitlines()
print("Alfavit bo‘yicha:", sorted(names))
