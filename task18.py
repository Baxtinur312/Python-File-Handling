with open("students.txt") as f:
    names = f.read().splitlines()
query = input("Ism kiriting: ")
if query in names:
    print("Ism mavjud.")
else:
    print("Ism topilmadi.")
