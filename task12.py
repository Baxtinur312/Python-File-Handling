def read_names():
    with open("students.txt") as f:
        return f.read().splitlines()

def task2():
    return len(read_names())

