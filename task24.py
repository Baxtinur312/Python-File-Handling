def task6():
    rows = read_grades()
    avg = sum(int(x[1]) for x in rows) / len(rows)
    return [x for x in rows if int(x[1]) > avg]