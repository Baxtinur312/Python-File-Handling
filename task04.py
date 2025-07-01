with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
juftlar = [n for n in numbers if n % 2 == 0]
print("Juft sonlar:", juftlar)
