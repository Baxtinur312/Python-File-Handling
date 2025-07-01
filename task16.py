def task16():
    with open("students.txt") as f:
        names = f.read().splitlines()
    long_names = [n for n in names if len(n) > 5]
    return long_names

