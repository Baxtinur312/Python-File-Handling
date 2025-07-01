def read_names():
    with open("students.txt") as f:
        return f.read().splitlines()

def task4():
    return list(reversed(read_names()))


