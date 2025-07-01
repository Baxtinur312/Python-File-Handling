with open("grades.csv") as f:
    students = [line.split(",") for line in f]
grades = [int(score) for _, score in students]
avg = sum(grades) / len(grades)
above_avg = [name for name, score in students if int(score) > avg]
print("O‘rtachadan yuqori olganlar:", above_avg)
