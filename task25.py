with open("grades.csv") as f:
    students = [line.split(",") for line in f]
with open("high_scores.csv", "w") as f:
    for name, grade in students:
        if grade.strip() == "5":
            f.write(f"{name},{grade}")
print("5 olganlar high_scores.csv fayliga yozildi.")
