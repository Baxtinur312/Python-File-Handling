with open("students.txt") as f:
    names = f.read().splitlines()
print("Ismlar soni:", len(names))
