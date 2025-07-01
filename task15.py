with open("students.txt") as f:
    names = f.read().splitlines()
for name in names:
    print(f"{name}: {len(name)} ta harf")
