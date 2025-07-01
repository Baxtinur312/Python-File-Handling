def task17():
    with open("students.txt") as f:
        names = f.read().splitlines()
    a_names = [n for n in names if n.lower().startswith("a")]
    with open("a_names.txt", "w") as f:
        for name in a_names:
            f.write(name + "\n")
    print("A harfi bilan boshlanuvchilar a_names.txt fayliga yozildi.")

    return a_names