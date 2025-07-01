with open("grades.csv") as f:
    students = [line.split(",") for line in f]
top_student = max(students, key=lambda x: int(x[1]))
print("Eng yuqori baho olgan:", top_student[0])
