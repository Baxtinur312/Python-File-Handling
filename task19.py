def task19():
    with open("grades.csv", "w") as f:
        f.write("Name,Grade\n")
        f.write("Alice,85\n")
        f.write("Bob,90\n")
        f.write("Charlie,78\n")
        f.write("David,92\n")
        f.write("Eve,88\n")
        return "grades.csv"

