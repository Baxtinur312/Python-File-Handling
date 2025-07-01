def task22():
    with open("grades.csv") as f:
        fives = [1 for line in f if line.endswith(",5")]
    print("5 olganlar soni:", sum(fives))
    return sum(fives)
