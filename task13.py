def read_names():
    with open("students.txt") as f:
        return f.read().splitlines()

def task3():
    return sorted(read_names())


