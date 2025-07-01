def task15():
    def read_names():
        with open("students.txt") as f:
            return f.read().splitlines()

    names = read_names()
    results = []
    for name in names:
        results.append(f"{name}: {len(name)} ta harf")
    
    return results


   
