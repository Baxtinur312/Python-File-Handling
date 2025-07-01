def read_numbers():
    with open("numbers.txt") as f:
        return list(map(int, f.read().split()))
nums = []
def task4():
    numbers = read_numbers()
    if numbers:
     beshliklar = [n for n in numbers if n % 5 == 0]
    nums += 1
    return beshliklar

