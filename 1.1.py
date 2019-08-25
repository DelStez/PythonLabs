# Составить программу, проверяющую, будут ли взаимно просты два натуральных (целых) числа.
f_number = int(input("Введите первое натуральное число: "))
s_number = int(input("Введите второе натуральное число: "))

d = 0
if s_number <= f_number:
    for i in range(1, f_number):
            if f_number % i == 0 and s_number % i == 0:
                d = i
    if not d == 1:
        k = "Числа не взаимно простые"
    else:
        k = "Числа взаимно простые"
    print(k)
else:
    for i in range(1, s_number):
            if f_number % i == 0 and s_number % i == 0:
                d = i
    if not d == 1:
        k = "Числа не взаимно простые"
    else:
        k = "Числа взаимно простые"
    print(k)
