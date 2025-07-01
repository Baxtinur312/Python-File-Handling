from numbers_tasks import (
    vazifa_1, vazifa_2, vazifa_3, vazifa_4, vazifa_5,
    vazifa_6, vazifa_7, vazifa_8, vazifa_9, vazifa_10, read_numbers
)
from students_tasks import (
    s_vazifa_1, s_vazifa_2, s_vazifa_3, s_vazifa_4,
    s_vazifa_5, s_vazifa_6, s_vazifa_7, s_vazifa_8, read_names
)
from grades_tasks import (
    g_vazifa_1, g_vazifa_2, g_vazifa_3, g_vazifa_4,
    g_vazifa_5, g_vazifa_6, g_vazifa_7, read_grades
)


def print_menu():
    print("""
======== MENU ========
1. Numbers.txt vazifalar
2. Students.txt vazifalar
3. Grades.csv vazifalar
0. Chiqish
""")


def numbers_menu():
    numbers = read_numbers()
    print("""
Numbers.txt vazifalar:
1 - Barcha sonlar
2 - Yig‘indi
3 - Eng katta son
4 - Juft sonlar
5 - O‘rtacha qiymat
6 - Toq sonlarni faylga yozish
7 - Kvadratlar
8 - 5 ga karralilar
9 - Son xonalari
10 - Tartiblab faylga yozish
""")
    choice = input("Vazifani tanlang (1-10): ")
    funcs = [
        vazifa_1, vazifa_2, vazifa_3, vazifa_4, vazifa_5,
        vazifa_6, vazifa_7, vazifa_8, vazifa_9, vazifa_10
    ]
    if choice.isdigit() and 1 <= int(choice) <= 10:
        funcs[int(choice) - 1](numbers)


def students_menu():
    names = read_names()
    print("""
Students.txt vazifalar:
1 - Ismlarni chiqarish
2 - Ismlar soni
3 - Alfavit bo‘yicha tartiblash
4 - Teskari tartibda chiqarish
5 - Harflar soni
6 - 5 harfdan uzunlar
7 - A harfi bilan boshlanuvchilarni faylga yozish
8 - Foydalanuvchi ismini tekshirish
""")
    choice = input("Vazifani tanlang (1-8): ")
    funcs = [
        s_vazifa_1, s_vazifa_2, s_vazifa_3, s_vazifa_4,
        s_vazifa_5, s_vazifa_6, s_vazifa_7, s_vazifa_8
    ]
    if choice.isdigit() and 1 <= int(choice) <= 8:
        funcs[int(choice) - 1](names)


def grades_menu():
    students = read_grades()
    print("""
Grades.csv vazifalar:
1 - Ism va baholarni chiqarish
2 - Baholar o‘rtachasi
3 - Eng yuqori baho olgan
4 - 5 olganlar soni
5 - Har bir baho soni (Counter)
6 - O‘rtachadan yuqori olganlar
7 - 5 olganlarni faylga yozish
""")
    choice = input("Vazifani tanlang (1-7): ")
    funcs = [
        g_vazifa_1, g_vazifa_2, g_vazifa_3, g_vazifa_4,
        g_vazifa_5, g_vazifa_6, g_vazifa_7
    ]
    if choice.isdigit() and 1 <= int(choice) <= 7:
        funcs[int(choice) - 1](students)


def main():
    while True:
        print_menu()
        tanlov = input("Bo‘limni tanlang (0-3): ")
        if tanlov == '1':
            numbers_menu()
        elif tanlov == '2':
            students_menu()
        elif tanlov == '3':
            grades_menu()
        elif tanlov == '0':
            print("Chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov.")


if __name__ == "__main__":
    main()
