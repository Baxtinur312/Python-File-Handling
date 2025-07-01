from collections import Counter
def task23():   
    with open("grades.csv") as f:
        grades = [int(line.split(",")[1]) for line in f]
    counts = Counter(grades)
    print("Baholar statistikasi:", dict(counts))
    return dict(counts)
