def task20():
    with open("grades.csv") as f:
        grades = [int(line.split(",")[1]) for line in f]
    avg = sum(grades) / len(grades)
    print("Baholar o‘rtachasi:", avg)
    return avg
