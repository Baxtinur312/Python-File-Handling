def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))

def task10():
    sorted_nums = sorted(read_numbers())
    with open("sorted_numbers.txt", "w") as f:
        for n in sorted_nums:
            f.write(str(n) + "\n")
    return sorted_nums
