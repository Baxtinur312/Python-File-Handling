def read_names():
    with open("students.txt") as f:
        return f.read().splitlines()

def task1():
    return read_names()


