with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
print("Eng katta son:", max(numbers))
