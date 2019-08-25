"""
Даны действительные числа a[0],..., a[6]. Получить для x = 1, 2, 3, 4 значения p(x+1)-p(x), где:
p(y) = a[1]*y6 + a[2]*y5 + a[3]*y4 + a[4]*y3 + ... + a[0].
"""
def p_y(x, a):
    s = a[0]
    for i in range(6, 0, -1):
        s = s + (a[i] * (x ** (7-i)))
    return s


n = 7
a = []
for i in range(n):
    a.append(float(input("Введите любое число: ")))
for x in range(4):
    print("Значение х=", p_y(x+1,a)-p_y(x,a))

