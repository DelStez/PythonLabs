""""
Дан файл f, компоненты которого являются действительными числами. Найти:
а) сумму компонент файла f;
б) произведение компонент файла f;
в) сумму квадратов компонент файла f;
г) модуль суммы и квадрат произведения компонент файла f;
д) последнюю компоненту файла;
"""

file_name = input("Введите название файла c расширением txt: ")
numbers_letters = int(input("Введите количество чисел в файле: "))

list_file = list()
for i in range(numbers_letters):
    number = float(input("Введите действительное число: "))
    list_file.append(number)
with open(file_name, "a") as f:
    for number in list_file:
        f.write(number)
f.close()

f = open(file_name, "r")
n = [line.strip() for line in f]
print(n)
f.close()
