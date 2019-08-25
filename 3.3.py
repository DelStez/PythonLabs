# Определите, равен ли "центральный" элемент числового списка произведению крайних элементов.


lista = [int(i) for i in input('Введите значения тут: ').split()]
print(lista)
if (len(lista) % 2 != 0):
    cen = lista[int((len(lista)) /2)]
    a = lista[0]
    b = lista[len(lista) - 1]
    if(a*b == cen):
        print("Равен")
    else:
        print("Неравен")
else:
    print("Центральный элемент отсутствует")
