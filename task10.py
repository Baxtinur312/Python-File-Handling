with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
with open("sorted_numbers.txt", "w") as f:
    for n in sorted(numbers):
        f.write(str(n) + "\n")
print("Saralangan sonlar sorted_numbers.txt fayliga yozildi.")
