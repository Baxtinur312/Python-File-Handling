with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
o_rta = sum(numbers) / len(numbers)
print("O‘rtacha qiymat:", o_rta)
