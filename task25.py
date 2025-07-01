
def task7():
    rows = read_grades()
    fives = [x for x in rows if x[1] == '5']
    with open("high_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(fives)
    return fives