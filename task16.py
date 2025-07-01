with open("students.txt") as f:
    names = f.read().splitlines()
long_names = [n for n in names if len(n) > 5]
print("5 harfdan uzun ismlar:", long_names)
