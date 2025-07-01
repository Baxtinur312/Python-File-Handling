with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
with open("odd_numbers.txt", "w") as f:
    for n in numbers:
        if n % 2 != 0:
            f.write(str(n) + "\n")
print("Toq sonlar odd_numbers.txt fayliga yozildi.")
