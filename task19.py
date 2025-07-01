with open("grades.csv") as f:
    lines = f.read().splitlines()
for line in lines:
    name, grade = line.split(",")
    print(f"{name}: {grade}")
