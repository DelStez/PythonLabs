# Дан список A из k элементов, каждый из которых является списком из m целых чисел.
# Построить список из m элементов, каждый элемент которого
# равен сумме элементов, стоящих на соответствующих местах в каждом из k элементов списка А.
import random

k = int(input("Введите количество элементов списка \"A\": "))
m = int(input("Введите количество элементов списка \"k\": "))
list_a = []
for x in range(k):
    list_m = []
    for q in range(m):
        list_m.append(random.randint(0, 10))
    list_a.append(list_m)
print(list_a)

list_z = []
for i in range(m):
    n = 0
    for j in range(k):
        pred_a = list_a[j]
        n += pred_a[i]
    list_z.append(n)
print(list_z)