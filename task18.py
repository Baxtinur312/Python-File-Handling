names = []
def task18():
    with open("students.txt") as f:
        names = f.read().splitlines()
    unique_names = set(input("Ismlar: ").split())
    if unique_names not in names:
        print("Bunday ism mavjud emas.")
    else:
        print(f"Bunday ism mavjud.{unique_names}")
    return unique_names
