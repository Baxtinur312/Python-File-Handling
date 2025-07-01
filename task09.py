with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
for n in numbers:
    xona = len(str(abs(n)))
    print(f"{n} — {xona} xonali")
