# По заданной формуле члена ряда с номером k составить две программы:
# а) программу вычисления суммы первых n членов заданного ряда;
n = int(input("Введите n-число: "))
s = 0.0
for k in range(1, n + 1):
    s += 1 / (((2 * k) - 1) * ((2 * k) + 1))
print(s)
# б)программу вычисления всех членов ряда, не меньших заданного числа E.
e = float(input("Введите число: "))
k = 1
s = 1 / (((2 * k) - 1) * ((2 * k) + 1))
if e <= 0:
    print("Введено некорректное значение")
else:
    if s <= e:
        print("Не осталось удовлетворяющих значений")
        quit()
while s >= e:
    s = 1 / (((2 * k) - 1) * ((2 * k) + 1))
    k += 1
    print(s)