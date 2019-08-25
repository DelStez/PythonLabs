# Определите индекс элемента числового списка,
# значение которого равно сумме первого и последнего элемента того же списка.

spisok = [int(i) for i in input('Введите значения тут: ').split()]
if not spisok:
    print("Список пуст")
else:
    summa = spisok[0] + spisok[len(spisok) - 1]
    n = 0
    for i in range(0, len(spisok)):
        if spisok[i] == summa:
            n = i
    if not n:
        print("Элемент отсутствует")
    else:
        print(n)
