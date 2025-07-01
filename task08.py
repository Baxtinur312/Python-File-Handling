with open("numbers.txt") as f:
    numbers = list(map(int, f.read().split()))
beshliklar = [n for n in numbers if n % 5 == 0]
print("5 ga karralilar:", beshliklar)
print("Ular soni:", len(beshliklar))
